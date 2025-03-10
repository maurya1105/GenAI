import logging
from logging.handlers import RotatingFileHandler
# from logging.handlers import TimedRotatingFileHandler
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms.ollama import Ollama
# from langchain_ollama.chat_models import ChatOllama
from concurrent.futures import ThreadPoolExecutor
from langchain_community.vectorstores import FAISS
from countrysheet import get_address_format_by_country_name_sheet
from apistate import get_states_by_country_name_api
import warnings
import torch
import time
import threading
from prompt_templates import PROMPT_TEMPLATE

# # Set up timed log rotation
# log_handler = TimedRotatingFileHandler(
#     filename='app.log',      # Log file name
#     when='midnight',         # Rotate logs at midnight
#     interval=1,              # Rotate every 1 day
#     backupCount=7,           # Keep 7 days of log files
#     encoding=None,         
#     delay=0                 
# )

# Set up logging
log_handler = RotatingFileHandler(
    filename='app.log',   
    mode='a',                # append mode
    maxBytes=50*1024*1024,    # 50 MB max per log file
    backupCount=3,           # 3 backup log files
    encoding=None,           # Default encoding
    delay=0                  # File is opened immediately
)

logging.basicConfig(
    handlers=[log_handler],
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
)

stop_loop = False

# Define a function to handle key press events
def on_press(key):
    global stop_loop
    try:
        if key.char == 'q':
            stop_loop = True
    except AttributeError:
        pass

executor = ThreadPoolExecutor()

def run_chain(chain, context_text, query_text, history, stop_flag):
    response_chunks = []
    for chunk in chain.stream({"context": context_text, "question": query_text, "history": history}):
        if stop_flag.is_set():  # Check if the loop should be stopped
            # print("Loop stopped.")
            break
        print(chunk, end="", flush=True)
        response_chunks.append(chunk)
    return "".join(response_chunks)


warnings.filterwarnings("ignore", category=FutureWarning, message="`resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.")

#temporarily mimics the llm stream effect
def stream_static_reply(static_reply):
    for char in static_reply:
        print(char, end="", flush=True)
        time.sleep(0.01)  # Adjust the delay as needed
    print() 

import re
def classify_with_nlp_checker(query_text):
    # Simple regex to check if 'work calendar' or a similar pattern is in the query
    return re.search(r"(configure|create)\s+(a\s+)?work[-\s]*calendar(\s+for\s+\w+.*)?", query_text, re.IGNORECASE) is not None


device = "cuda" if torch.cuda.is_available() else "cpu"
print("Device: ", device)
logging.info(f"Device selected: {device}")

kArray=[5,2,1]

# @profile
def load_model():
    global model
    try:
        model = Ollama(model="llama3:instruct", temperature=0, keep_alive=-1)
        logging.info("Ollama model initialized successfully.")
    except Exception as e:
        logging.critical(f"Failed to initialize Ollama model: {e}")
        raise
    # model = ChatOllama(model="llama3:instruct", temperature=0, keep_alive=0, seed=42)

# @profile
def load_embedding():
    global embedding_function
    try:
        embedding_function = HuggingFaceEmbeddings(model_name='sentence-transformers/all-mpnet-base-v2', model_kwargs={"device": device})
        logging.info("Embedding function loaded successfully.")
    except Exception as e:
        logging.critical(f"Failed to load embedding function: {e}")
        raise

# @profile
def load_faiss():
    global db, db_tbl
    try:
        db = FAISS.load_local("faiss_index", embedding_function, allow_dangerous_deserialization=True)
        logging.info("FAISS index 'db' loaded successfully.")
    except Exception as e:
        logging.critical(f"Failed to load FAISS index 'db': {e}")
        raise

    try:
        db_tbl = FAISS.load_local("faiss_index_tbl", embedding_function, allow_dangerous_deserialization=True)
        logging.info("FAISS index 'db_tbl' loaded successfully.")
    except Exception as e:
        logging.critical(f"Failed to load FAISS index 'db_tbl': {e}")
        raise

def build_context(results):
    context_texts = []

    def process_result(doc_score):
        doc, _score = doc_score
        return doc.page_content

    with ThreadPoolExecutor() as executor:
        context_texts = list(executor.map(process_result, results))

    context_text = "\n\n---\n\n".join(context_texts)
    logging.debug(f"Built context: {context_text[:100]}...")  # Log the first 100 characters for brevity
    return context_text


# @profile
def query_rag(query_text, history, prompt_index):
    context_text = ""
    if prompt_index == 0:
        dbt = db
    else:
        dbt = db_tbl

    logging.info(f"Query: {query_text}")
    try:
        future_results_tbl = executor.submit(dbt.similarity_search_with_score, query_text, k=kArray[prompt_index])
        results = future_results_tbl.result()
        logging.debug(f"Search results obtained: {len(results)} documents.")
    except Exception as e:
        logging.error(f"Error during similarity search: {e}")
        return ["Error during query processing.", []]
    
    context_text = build_context(results)

    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE[prompt_index])
    chain = prompt | model | StrOutputParser()

    stop_flag=threading.Event()
    future = executor.submit(run_chain, chain, context_text, query_text, history, stop_flag)

    while not future.done():
        if stop_loop:
            stop_flag.set()  # Signal the chain to stop
            print("\n\nStopping response generation...")
            logging.info("Stopping response generation...")

            break
        time.sleep(0.01)  # Check periodically

    # Wait for the response to complete if it hasn't already
    if future.done():
        response_text = future.result()
    else:
        response_text = "Response generation was interrupted."

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    logging.info(f"Response generated: {response_text[:100]}...")  # Log the first 100 characters

    return [response_text, sources]


def query(query_text, prompt_index, history=None, address_format=None):    

    logging.info(f"Running query with prompt index {prompt_index}")
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE[prompt_index])
    chain= prompt | model | StrOutputParser()
    
    response_chunks = []
    try:
        if address_format:
            for chunk in chain.stream({"question":query_text, "address_format":address_format, "history":history}):
                print(chunk, end="", flush=True)
                response_chunks.append(chunk)
        else:
            for chunk in chain.stream({"question":query_text, "history":history}):
                print(chunk, end="", flush=True)
                response_chunks.append(chunk)
    except Exception as e:
            logging.error(f"Error during query processing: {e}")

    response_text = "".join(response_chunks)
    logging.info(f"Response: {response_text[:100]}...")  # Log the first 100 characters
    return [response_text]

if __name__ == "__main__":
    
    logging.info("Application started.")
    inp=""
    history=[]
    response=""
    ind=0
    pfs=["C2M info","DB info","DB config help", "Country config"]
    
    
    load_model()
    load_embedding()
    load_faiss()

    print("Enter 'quit' to exit")
    print("Enter: \n pf0 for C2M info \n pf1 for DB info \n pf2 for DB config help \n pf3 for Country config \n\nDefault prompt template is C2M info")
    while(True):
        stop_loop = False
        inp=input("\nQuery: ")
        if(inp=="quit"):
            logging.info("Exiting application.")
            break
        if(inp=="pf0"or inp=="pf1" or inp=="pf2" or inp=="pf3"):
            ind=int(inp[-1])
            logging.info(f"Prompt Format selected: {pfs[ind]}")
            print("Prompt Format: ",pfs[ind])
            continue
        
        history.append({"role":"user","content":inp})
        try:
            if ind==3:
                insert_ci_country, insert_ci_country_l = get_address_format_by_country_name_sheet(inp)
                # response=query(inp, ind, str(history), address_format)
                
                #To be updated with a model that can provide accurate results for country config
                response=f"""
Response:  Here are the two SQL `INSERT` queries for country {inp}:

**CI_COUNTRY_L**
```sql
{insert_ci_country_l}
```
`CI_COUNTRY_L` contains labels for address fields.

**CI_COUNTRY**
```sql
{insert_ci_country}
```
`CI_COUNTRY` contains usage flags (required, not allowed, optional) and availability values (yes, no) for address fields. If a field's usage is `REQ` or `OPT`, `_AVAIL` should be `Y`. If `NA`, `_AVAIL` should be `N`.

"""         
                states_country = get_states_by_country_name_api(inp)
                response+=f"Here are the two SQL `INSERT` queries for the states in country {inp}:\n\n**CI_STATE**\n```sql\n{states_country[0]}```\n\n**CI_STATE_L**\n```sql\n{states_country[1]}```\n\nNumber of states in country {inp}: {states_country[2]}"
             
                stream_static_reply(response)

                history.append({"role":"assistant","content":response,"sources":""})
            elif ind==2 and classify_with_nlp_checker(inp):
                print(classify_with_nlp_checker(inp))
                #routing to prompt for work calendar -- API needed for holidays
                response = query(inp, 4, str(history))
                history.append({"role": "assistant", "content": response[0], "sources": " "})

            else:
                response=query_rag(inp,str(history),ind)
                print("\nSources: ",response[1])
                history.append({"role":"assistant","content":response[0],"sources":response[1]})
        except Exception as e:
            logging.critical(f"Critical error in main loop: {e}")

        while True:
            if ind!=3:
                follow_up_choice = input("\nDo you want to (1) ask a follow-up question or (2) start a new conversation? (Enter 1 or 2): ")
            else:
                follow_up_choice = "2"
            if follow_up_choice == "1":
                follow_up_query = input("\nFollow-up Query: ")
                try:
                    response = query(follow_up_query, 3, str(history))
                    
                    history.append({"role": "user", "content": follow_up_query})
                    history.append({"role": "assistant", "content": response[0], "sources": " "})
                except Exception as e:
                    logging.error(f"Error processing follow-up query: {e}")

            elif follow_up_choice == "2":
                history = []
                break
            else:
                logging.warning("Invalid follow-up choice made.")
                print("Invalid choice. Please enter 1 or 2.")

    logging.info("Application exited.")   
    print("Exiting...")
    executor.shutdown() 
    




