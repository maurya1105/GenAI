import argparse
import os
import shutil
import concurrent.futures
from datetime import datetime
import warnings
import torch
import markdown
import faiss

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.docstore.in_memory import InMemoryDocstore
from langchain.schema.document import Document
from langchain_community.vectorstores import FAISS

from get_embedding_function2 import get_embedding_function
from image_functions import save_images, process_images_with_ocr
from extract_info import extract_files, extract_from_pdf, extract_from_html, decompile_class_files, convert_ppt_to_pdf

torch.cuda.empty_cache()

warnings.filterwarnings("ignore", category=FutureWarning, message="`resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.")

DATA_PATH = "data"
IMAGE_PATH = "images"
FILE_STRUCTURE_PATH = "file_structures"
FAISS_PATH="faiss_index"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    parser.add_argument("--add-new", action="store_true", help="Add only new documents to the database.")
    args = parser.parse_args()

    if args.reset:
        print("✨ Clearing Database")
        clear_database()

    if args.reset or args.add_new:

        extract_files()
        documents, images = load_documents()
        if images:
            save_images(images)
            documents = process_images_with_ocr(images, documents)
        
        chunks = split_documents(documents)
        add_to_faiss(chunks, args.add_new)
    

def load_documents():
    documents = []
    images = []
    supported_extensions = (".pdf", ".csv", ".txt", ".html", ".java", ".xml", ".properties", ".md" ,".class", ".ppt", ".pptx", ".jsp", ".jspx", ".js", ".json")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for root, dirs, files in os.walk(DATA_PATH):
            for file in files:
                if file.endswith(supported_extensions):
                    file_path = os.path.join(root, file)
                    futures.append(executor.submit(load_document, file_path))
        
        for future in concurrent.futures.as_completed(futures):
            doc, img = future.result()
            if doc:
                documents.extend(doc)
            if img:
                images.extend(img)

    # for root, dirs, files in os.walk("file_structurescopy"): #needs to be changed
    #     for file in files:
    #         if file.endswith("_structure.json"):
    #             file_path = os.path.join(root, file)
    #             with open(file_path, 'r') as f:
    #                 structure = f.read()
    #                 metadata = {"source": file_path}
    #                 document = Document(page_content=structure, metadata=metadata)
    #                 documents.append(document)
    #     print("Added file structure")

    #UNCOMMENT LATER

    return documents, images


def load_document(file_path):
    documents = []
    images = []
    try:
        if file_path.endswith(".pdf"):
            doc_texts, doc_images = extract_from_pdf(file_path)
            documents.extend(doc_texts)
            images.extend(doc_images)
        elif file_path.endswith(".csv"):
            csv_loader = CSVLoader(file_path=file_path)
            documents.extend(csv_loader.load())
        elif file_path.endswith(".html"):
            documents.extend(extract_from_html(file_path))
        elif file_path.endswith(".class"):
            documents.extend(decompile_class_files(file_path))
        elif file_path.endswith(".md"): 
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                html = markdown.markdown(text)
                metadata = {"source": file_path}
                document = Document(page_content=html, metadata=metadata)
                documents.append(document)
        elif file_path.endswith(".txt") or file_path.endswith(".jsp") or file_path.endswith(".jspx") or file_path.endswith(".java") or file_path.endswith(".xml") or file_path.endswith(".properties") or file_path.endswith(".js") or file_path.endswith(".json"):
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                metadata = {"source": file_path}
                document = Document(page_content=text, metadata=metadata)
                documents.append(document)
        elif file_path.endswith(".ppt") or file_path.endswith(".pptx"):
            pdf_path = convert_ppt_to_pdf(file_path)
            if pdf_path:
                doc_texts, doc_images = extract_from_pdf(pdf_path)
                documents.extend(doc_texts)
                images.extend(doc_images)
    except Exception as e:
        print(f"Failed to load document {file_path}: {e}")
    return documents, images


separator="---------------------------------------------------------------------------"

def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
        separators=[separator],
        keep_separator=True,
        is_separator_regex=False
    )

    chunks = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_chunks = {executor.submit(text_splitter.split_documents, [doc]): doc for doc in documents}
        for future in concurrent.futures.as_completed(future_chunks):
            chunks.extend(future.result())
    
    return chunks


def add_to_faiss(chunks: list[Document], only_new=False, batch_size=100):
    try:
        db = FAISS.load_local("faiss_index", get_embedding_function(), allow_dangerous_deserialization=True)
        print(f"Loaded existing FAISS index with {db.index.ntotal} documents.")

    except Exception as e:
        print(f"No existing FAISS index. Creating one..")
        db = None
        print(f"👉 Adding {len(chunks)} documents")

    chunks_to_add = calculate_chunk_ids(chunks)
    total_chunks = len(chunks_to_add)

    if only_new and db is not None:
        existing_items = db.index_to_docstore_id
        existing_ids = set()
        
        for idx, doc_id in existing_items.items():
            if doc_id in db.docstore._dict:
                existing_ids.add(db.docstore._dict[doc_id].metadata["id"])

        print(f"Number of existing documents in DB: {len(existing_ids)}")

        new_chunks = []
        for chunk in chunks_to_add:
            if chunk.metadata["id"] not in existing_ids:
                new_chunks.append(chunk)
            else:
                print(f"Skipping duplicate document: {chunk.metadata['id']}")

        if len(new_chunks) > 0:
            print(f"👉 Adding {len(new_chunks)} new documents")
            for i in range(0, len(new_chunks), batch_size):
                batch = new_chunks[i:i + batch_size]
                print(f"Adding batch {i // batch_size + 1}/{(len(new_chunks) + batch_size - 1) // batch_size}")
                db.add_documents(batch)
        else:
            print("✅ No new documents to add")
    else:
        
        print(f"👉 Adding all {total_chunks} documents")
        for i in range(0, total_chunks, batch_size):
            batch = chunks_to_add[i:i + batch_size]
            print(f"Adding batch {i // batch_size + 1}/{(total_chunks + batch_size - 1) // batch_size}")
            if db is None:
                
                embedding_function = get_embedding_function()
                sample_embedding = embedding_function.embed_documents([chunks[0].page_content])[0]
                d = len(sample_embedding)  # Dimension of embeddings
                # print("d: ", d)
                hnsw_index = faiss.IndexHNSWFlat(d, 32)  # 32 = no. of neighbors
                
                docstore = InMemoryDocstore()
                index_to_docstore_id = {}
                db = FAISS(embedding_function=embedding_function, index=hnsw_index, docstore=docstore, index_to_docstore_id=index_to_docstore_id)
                db.add_documents(batch)
            else:
                db.add_documents(batch)

    db.save_local("faiss_index")
    print(f"\nTotal documents in the FAISS index: {db.index.ntotal}")


def calculate_chunk_ids(chunks):
    last_page_id = None
    current_chunk_index = 0
    chunks_with_ids = []

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        chunk.metadata["id"] = chunk_id
        chunks_with_ids.append(chunk)

    return chunks_with_ids



def clear_database():
    if os.path.exists(FAISS_PATH):
        shutil.rmtree(FAISS_PATH)
    if os.path.exists(IMAGE_PATH):
        shutil.rmtree(IMAGE_PATH)
    if os.path.exists(FILE_STRUCTURE_PATH):
        shutil.rmtree(FILE_STRUCTURE_PATH)


if __name__ == "__main__":
    start_time = datetime.now()
 
    main()
    
    end_time = datetime.now()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time}")