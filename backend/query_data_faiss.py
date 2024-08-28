from langchain_community.vectorstores import FAISS
from langchain_community.llms.ollama import Ollama
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.runnables import RunnablePassthrough
CHROMA_PATH = "chroma_clean_768"

PROMPT_TEMPLATE='''
###[INST]
Instruction: Answer the question based on your knowledge. Here is context to help:

{context}

### Here is the history of your conversation: 

{question}

Format answers properly, use only unordered lists whenever necessary, do not add any additional information to the answer that is not present in the context.

If you do not know the answer, just say you don't know, dont try to make up an answer.

[/INST]
'''
model = Ollama(model="mistral")

embedding_function =HuggingFaceEmbeddings(model_name='sentence-transformers/all-mpnet-base-v2',model_kwargs={ "device":"cuda" })

db = FAISS.load_local("faiss_index", embedding_function, allow_dangerous_deserialization=True)

#Retriver for RAG
retriever = db.as_retriever()

prompt = PromptTemplate(input_variables=["context", "question"],template=PROMPT_TEMPLATE)

llm_chain = LLMChain(llm=model, prompt=prompt)

rag_chain = ({"context": retriever, "question": RunnablePassthrough()}| llm_chain)

def query_rag(query_text: str,history):

    x=rag_chain.invoke(str(history)+"\n\n### Question:\n\n"+query_text)

    y= db.similarity_search(query_text, k=3)
    print(x)
    response_text=x["text"]

    sources =[doc.metadata.get("id") for doc in x["context"]]
    sources.extend([doc.metadata.get("id") for doc in y])

    return [response_text,sources]


