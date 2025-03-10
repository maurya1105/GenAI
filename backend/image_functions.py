import os
import concurrent.futures
import cv2
import pytesseract
from langchain.schema.document import Document

IMAGE_PATH = "images"

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
            # print(text)
            return Document(page_content=text, metadata={"source": image_name, "page": idx})
    except Exception as e:
        print(f"Failed to OCR image {image_name}: {e}")
    return None