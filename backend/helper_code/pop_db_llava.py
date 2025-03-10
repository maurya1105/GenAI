import argparse
import os
import shutil
import fitz  # PyMuPDF
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from get_embedding_function import get_embedding_function
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders.text import TextLoader
import concurrent.futures
import requests
import base64
import json


CHROMA_PATH = "chroma"
DATA_PATH = "data"
IMAGE_PATH = "images"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    parser.add_argument("--add-new", action="store_true", help="Add only new documents to the database.")
    args = parser.parse_args()

    if args.reset:
        print("✨ Clearing Database")
        clear_database()

    if args.reset or args.add_new:
        documents, images = load_documents()
        save_images(images)
        documents=process_images_with_llava(images, documents)
        chunks = split_documents(documents)
        add_to_chroma(chunks, args.add_new)
        
        


def load_documents():
    documents = []
    images = []

    for filename in os.listdir(DATA_PATH):
        file_path = os.path.join(DATA_PATH, filename)
        if file_path.endswith(".pdf"):
            doc_texts, doc_images = extract_from_pdf(file_path)
            documents.extend(doc_texts)
            images.extend(doc_images)
        elif file_path.endswith(".csv"):
            csv_loader = CSVLoader(file_path=file_path)
            documents.extend(csv_loader.load())
        elif file_path.endswith(".txt"):
            text_loader = TextLoader(file_path=file_path)
            documents.extend(text_loader.load())

    return documents, images


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

    with concurrent.futures.ProcessPoolExecutor() as executor:
        chunks = list(executor.map(text_splitter.split_documents, [documents]))

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

    for document_chunks in chunks:
        for chunk in document_chunks:
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
    for image_name, image_bytes in images:
        image_path = os.path.join(IMAGE_PATH, image_name)
        with open(image_path, "wb") as img_file:
            img_file.write(image_bytes)
# Define your generate_text function to accept image name and image bytes

api_endpoint = "http://localhost:11434/api/generate"

def process_images_with_llava(images, documents):
    image_files = os.listdir(IMAGE_PATH)
    i=0
    for image_name in image_files:
        
        image_path = os.path.join(IMAGE_PATH, image_name)
        with open(image_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode()

        # Define the prompt for the model
        prompt = "Write me a description of the image/diagram and if it contains text convert image to text."

        # Prepare the payload for the POST request
        payload = {
            "model": "llava",
            "prompt": prompt,
            "images": [image_data]
        }

        # Send the POST request
        response = requests.post(api_endpoint, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            generated_text = ""
            for item in response.iter_lines():
                item = json.loads(item)
                generated_text += item.get("response", "")
            # Print the generated text
            print("Generated Text:", generated_text)
            document = Document(page_content=generated_text, metadata={"source": image_name, "page": i})  # Create Document object
            documents.append(document)
            i+=1
        else:
            print("Error:", response.text)

    return documents


def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    if os.path.exists(IMAGE_PATH):
        shutil.rmtree(IMAGE_PATH)


if __name__ == "__main__":
    main()
