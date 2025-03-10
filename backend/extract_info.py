import os
# import comtypes.client
import markdownify
import subprocess
import zipfile
import fitz  # PyMuPDF
import json
# import pythoncom
from langchain.schema.document import Document

DATA_PATH = "data"
FILE_STRUCTURE_PATH = "file_structures"
cfr_jar_path = 'cfr-0.152.jar'
java_path = 'C:\\Program Files\\Java\\jdk-18.0.2.1\\bin\\java.exe'

def extract_files():
    file_structures = {}
    for filename in os.listdir(DATA_PATH):
        file_path = os.path.join(DATA_PATH, filename)
        if file_path.endswith(('.ear', '.jar', '.war', '.zip')):
            extract_to = os.path.join(DATA_PATH, filename[:-4])
            os.makedirs(extract_to, exist_ok=True)
            extract_archive(file_path, extract_to)
            file_structures[filename] = get_directory_structure(extract_to)
    
    save_file_structures(file_structures)


def extract_archive(file_path, extract_to):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)


def get_directory_structure(rootdir):
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


def convert_ppt_to_pdf(file_path):

    absolute_file_path = os.path.abspath(file_path)
    output_file_path = absolute_file_path.rsplit('.', 1)[0]  + ".pdf"

    pythoncom.CoInitialize()

    try:
        powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
        powerpoint.Visible = 1
        slides = powerpoint.Presentations.Open(absolute_file_path)
        slides.SaveAs(output_file_path, 32) 
        slides.Close()
        powerpoint.Quit()
        print(f"Converted PDF saved at: {output_file_path}")
        return output_file_path
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pythoncom.CoUninitialize()
   
def convert_doc_to_pdf(file_path):
    # Convert to absolute path
    absolute_file_path = os.path.abspath(file_path)
    # Prepare output file path
    output_file_path = absolute_file_path.rsplit('.', 1)[0] + ".pdf"

    # Debug: Print file paths
    print(f"Absolute file path: {absolute_file_path}")
    print(f"Output file path: {output_file_path}")

    # Initialize COM library
    pythoncom.CoInitialize()

    try:
        # Create Word application object
        word = comtypes.client.CreateObject("Word.Application")
        word.Visible = False  # Make Word invisible

        # Open the document
        doc = word.Documents.Open(absolute_file_path)
        
        # Save the document as PDF
        doc.SaveAs(output_file_path, FileFormat=17)  # 17 = PDF
        
        # Close the document and Word application
        doc.Close()
        word.Quit()

        print(f"Converted PDF saved at: {output_file_path}")
        return output_file_path
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Uninitialize COM library
        pythoncom.CoUninitialize()

def extract_from_html(file_path):
    documents = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            markdown_text = markdownify.markdownify(text)
            metadata = {"source": file_path}
            document = Document(page_content=markdown_text, metadata=metadata)
            documents.append(document)
         
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
      
    except Exception as e:
        print(f"Exception: {str(e)}")

    return documents, images  

def decompile_class_files(file_path):
    documents = []
    try:
        output = subprocess.check_output([java_path, '-jar', cfr_jar_path, file_path], stderr=subprocess.STDOUT)
        text=output.decode('utf-8')
        # print(text)
        if text:
            metadata = {"source": file_path, "page": 0}
            document = Document(page_content=text, metadata=metadata)
            documents.append(document)
    except FileNotFoundError as e:
        print(f"File not found during decompilation: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Decompilation failed: {e.output.decode('utf-8')}")
    return documents

# import re
# file="data\C2M\C2M\01_Overview\EDAG_01_Overview.docx"
# formatted_file_path = file.replace('\\', '/')
# print(formatted_file_path)
# # convert_doc_to_pdf(formatted_file_path)