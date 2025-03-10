import argparse
import os
import shutil
import zipfile
import fitz  # PyMuPDF
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from get_embedding_function2 import get_embedding_function
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders.text import TextLoader
import concurrent.futures
import cv2
import pytesseract
import json
from datetime import datetime
import warnings
import markdownify
warnings.filterwarnings("ignore", category=FutureWarning, message="`resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.")


CHROMA_PATH = "chroma"
DATA_PATH = "data"
IMAGE_PATH = "images"
FILE_STRUCTURE_PATH = "file_structures"


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
        save_images(images)
        documents = process_images_with_ocr(images, documents)
        chunks = split_documents(documents)
        add_to_chroma(chunks, args.add_new)



def extract_files():
    file_structures = {}
    for filename in os.listdir(DATA_PATH):
        file_path = os.path.join(DATA_PATH, filename)
        if file_path.endswith(('.ear', '.jar', '.war')):
            extract_to = os.path.join(DATA_PATH, filename[:-4])
            os.makedirs(extract_to, exist_ok=True)
            extract_archive(file_path, extract_to)
            file_structures[filename] = get_directory_structure(extract_to)
    
    save_file_structures(file_structures)


def extract_archive(file_path, extract_to):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


def get_directory_structure(rootdir):
    """
    Creates a dictionary representing the folder structure of rootdir
    """
    dir_structure = {}
    for dirpath, dirnames, filenames in os.walk(rootdir):
        dirpath = dirpath.replace(rootdir, '').lstrip(os.sep)
        subdir = dir_structure
        if dirpath:
            for part in dirpath.split(os.sep):
                subdir = subdir.setdefault(part, {})
        for dirname in dirnames:
            subdir[dirname] = {}
        for filename in filenames:
            subdir[filename] = "__file__"
    return dir_structure


def save_file_structures(file_structures):
    os.makedirs(FILE_STRUCTURE_PATH, exist_ok=True)
    for filename, structure in file_structures.items():
        structure_path = os.path.join(FILE_STRUCTURE_PATH, f"{filename}_structure.json")
        with open(structure_path, 'w') as f:
            json.dump(structure, f, indent=2)


def load_documents():
    documents = []
    images = []
    supported_extensions = (".pdf", ".csv", ".txt", ".html", ".java", ".xml", ".properties")

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
    # print("reached fun lds")
    # Load the file structures as documents
    for root, dirs, files in os.walk("file_structurescopy"):
        for file in files:
            if file.endswith("_structure.json"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    structure = f.read()
                    metadata = {"source": file_path}
                    document = Document(page_content=structure, metadata=metadata)
                    documents.append(document)
        print("Added file structure")

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
        elif file_path.endswith(".txt") or file_path.endswith(".jsp") or file_path.endswith(".jspx") or file_path.endswith(".java") or file_path.endswith(".xml") or file_path.endswith(".properties") or file_path.endswith(".js"):
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                metadata = {"source": file_path}
                document = Document(page_content=text, metadata=metadata)
                documents.append(document)
    except Exception as e:
        print(f"Failed to load document {file_path}: {e}")
    return documents, images

def extract_from_html(file_path):
    documents = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            markdown_text = markdownify.markdownify(text)
            metadata = {"source": file_path}
            document = Document(page_content=markdown_text, metadata=metadata)
            documents.append(document)
            # print("Extracted html")
    except Exception as e:
        print(f"Failed to extract from HTML {file_path}: {e}")
    return documents

def extract_from_pdf(file_path):
    documents = []
    images = []
    try:
        doc = fitz.open(file_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()
            if text:
                metadata = {"source": file_path, "page": page_num}
                document = Document(page_content=text, metadata=metadata)
                documents.append(document)

            image_list = page.get_images(full=True)
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]
                image_name = f"{os.path.basename(file_path)}_page{page_num}_{img_index}.{image_ext}"
                images.append((image_name, image_bytes))
        # print("Extracted pdf")
    except Exception as e:
        print(f"Exception: {str(e)}")

    return documents, images


def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )

    chunks = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_chunks = {executor.submit(text_splitter.split_documents, [doc]): doc for doc in documents}
        for future in concurrent.futures.as_completed(future_chunks):
            chunks.extend(future.result())
    
    return chunks


def add_to_chroma(chunks: list[Document], only_new=False, batch_size=100):
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )

    chunks_with_ids = calculate_chunk_ids(chunks)

    if only_new:
        existing_items = db.get(include=[])
        existing_ids = set(existing_items["ids"])
        print(f"Number of existing documents in DB: {len(existing_ids)}")

        new_chunks = [chunk for chunk in chunks_with_ids if chunk.metadata["id"] not in existing_ids]

        if len(new_chunks):
            print(f"👉 Adding new documents: {len(new_chunks)}")
            for i in range(0, len(new_chunks), batch_size):
                batch = new_chunks[i:i+batch_size]
                print(f"Adding batch {i//batch_size + 1}/{len(new_chunks)//batch_size + 1}")
                new_chunk_ids = [chunk.metadata["id"] for chunk in batch]
                db.add_documents(batch, ids=new_chunk_ids)
        else:
            print("✅ No new documents to add")
    else:
        print(f"👉 Adding all documents: {len(chunks_with_ids)}")
        for i in range(0, len(chunks_with_ids), batch_size):
            batch = chunks_with_ids[i:i+batch_size]
            print(f"Adding batch {i//batch_size + 1}/{len(chunks_with_ids)//batch_size + 1}")
            chunk_ids = [chunk.metadata["id"] for chunk in batch]
            db.add_documents(batch, ids=chunk_ids)


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


def save_images(images):
    os.makedirs(IMAGE_PATH, exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(save_image, image_name, image_bytes) for image_name, image_bytes in images]
        for future in concurrent.futures.as_completed(futures):
            future.result()


def save_image(image_name, image_bytes):
    try:
        image_path = os.path.join(IMAGE_PATH, image_name)
        with open(image_path, "wb") as img_file:
            img_file.write(image_bytes)
    except Exception as e:
        print(f"Failed to save image {image_name}: {e}")


def process_images_with_ocr(images, documents):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(ocr_image, image_name, image_bytes, idx) for idx, (image_name, image_bytes) in enumerate(images)]
        for future in concurrent.futures.as_completed(futures):
            document = future.result()
            if document:
                documents.append(document)
    return documents


def ocr_image(image_name, image_bytes, idx):
    try:
        image_path = os.path.join(IMAGE_PATH, image_name)
        with open(image_path, "wb") as img_file:
            img_file.write(image_bytes)

        image = cv2.imread(image_path)
        text = pytesseract.image_to_string(image)
        if text:
            return Document(page_content=text, metadata={"source": image_name, "page": idx})
    except Exception as e:
        print(f"Failed to OCR image {image_name}: {e}")
    return None


def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    if os.path.exists(IMAGE_PATH):
        shutil.rmtree(IMAGE_PATH)
    if os.path.exists(FILE_STRUCTURE_PATH):
        shutil.rmtree(FILE_STRUCTURE_PATH)


if __name__ == "__main__":
    start_time = datetime.now()
    formatted_start_time = start_time.strftime("%H:%M:%S")
    print(f"Start time: {formatted_start_time}")
    
    main()
    end_time = datetime.now()
    formatted_end_time = end_time.strftime("%H:%M:%S")
    print(f"End time: {formatted_end_time}")

    execution_time = end_time - start_time
    formatted_execution_time = str(execution_time)
    print(f"Execution time: {formatted_execution_time}")
