from langchain_community.vectorstores import Chroma
from langchain_community.llms.ollama import Ollama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from concurrent.futures import ThreadPoolExecutor

CHROMA_PATH = "chroma_clean_768"

PROMPT_TEMPLATE="""
You are a knowledgeable assistant. Answer the question based on the following context:
 
{context}
 
Question: {question}
Answer in detail:
"""
model = Ollama(model="mistral")

embedding_function =HuggingFaceEmbeddings(model_name='sentence-transformers/all-mpnet-base-v2',model_kwargs={ "device":"cuda" })

db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)


def query_rag(query_text: str,history):
    with ThreadPoolExecutor() as executor:
        future_results = executor.submit(db.similarity_search_with_score, query_text, k=3)
        results = future_results.result()
    context_texts = []

    def process_result(doc_score):
        doc, _score = doc_score
        return doc.page_content

    with ThreadPoolExecutor() as executor:
        context_texts = list(executor.map(process_result, results))

    context_text = "\n\n---\n\n".join(context_texts)

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model="mistral")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]

    return [response_text,sources]


