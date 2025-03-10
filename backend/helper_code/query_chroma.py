import argparse
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from concurrent.futures import ThreadPoolExecutor
import warnings
from get_embedding_function2 import get_embedding_function
from datetime import datetime

warnings.filterwarnings("ignore", category=FutureWarning, message="`resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.")

CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
You are a knowledgeable assistant. Answer the question based on the following context:

{context}

Question: {question}
Answer in detail:
"""

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)
    

def build_context(results):
    context_texts = []

    def process_result(doc_score):
        doc, _score = doc_score
        return doc.page_content

    with ThreadPoolExecutor() as executor:
        context_texts = list(executor.map(process_result, results))

    context_text = "\n\n---\n\n".join(context_texts)
    return context_text



def query_rag(query_text: str):
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB in parallel
    with ThreadPoolExecutor() as executor:
        future_results = executor.submit(db.similarity_search_with_score, query_text, k=5)
        results = future_results.result()

    # Build context in parallel
    context_text = build_context(results)

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model="mistral")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\n\nSources: {sources}"
    print(formatted_response)
    return response_text



if __name__ == "__main__":
    start_time = datetime.now()
    main()
    end_time = datetime.now()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time}")


