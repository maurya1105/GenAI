from langchain_community.vectorstores import FAISS
from get_embedding_function import get_embedding_function
import json

FAISS_PATH = "faiss_index"

def load_faiss_index():
    try:
        db = FAISS.load_local(FAISS_PATH, get_embedding_function(), allow_dangerous_deserialization=True)
        print("FAISS index loaded successfully.")
        return db
    except Exception as e:
        print(f"Failed to load FAISS index: {e}")
        return None

def inspect_faiss_index(db):
    if db is None:
        return
    
    # Check the number of vectors in the index
    num_vectors = db.index.ntotal
    print(f"Number of vectors in the index: {num_vectors}")

    # Check the dimensionality of the vectors
    d = db.index.d
    print(f"Dimensionality of the vectors: {d}")

    # Check some metadata (assuming metadata exists in the docstore)
    if hasattr(db, 'docstore') and hasattr(db.docstore, '_dict'):
        print("Inspecting metadata of first 10 documents:")
        for i, (doc_id, doc) in enumerate(db.docstore._dict.items()):
            if i >= 10:
                break
            print(f"Document ID: {doc_id}")
            print(f"Metadata: {json.dumps(doc.metadata, indent=2)}")
            print(f"Content snippet: {doc.page_content[:100]}...")
            print("")

def main():
    db = load_faiss_index()
    inspect_faiss_index(db)

if __name__ == "__main__":
    main()
