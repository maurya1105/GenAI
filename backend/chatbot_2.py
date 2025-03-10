import os
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
from config_data import get_or_update_work_cal
from llm_sublayer import classify_query_object_category, work_cal_country_extract, extract_country_from_query

import warnings
import torch
import time
import threading
from pynput import keyboard
from dotenv import load_dotenv
from prompt_templates import PROMPT_TEMPLATE
import object_categories

warnings.filterwarnings("ignore", category=FutureWarning, message="`resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.")

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
        #Hit esc to stop generation
        if key == keyboard.Key.esc:
            stop_loop = True
    except AttributeError:
        pass

# Set up the listener for key press events
listener = keyboard.Listener(on_press=on_press)
listener.start()

executor = ThreadPoolExecutor()

def run_chain(chain, query_text, history, stop_flag, context_text=None):
    response_chunks = []
    if context_text:
        for chunk in chain.stream({"context": context_text, "question": query_text, "history": history}):
            if stop_flag.is_set():  # Check if the loop should be stopped
                # print("Loop stopped.")
                break
            print(chunk, end="", flush=True)
            response_chunks.append(chunk)
    else:
        for chunk in chain.stream({"question": query_text, "history": history}):
            if stop_flag.is_set():  # Check if the loop should be stopped
                # print("Loop stopped.")
                break
            print(chunk, end="", flush=True)
            response_chunks.append(chunk)

    return "".join(response_chunks)

#temporarily mimics the llm stream effect
def stream_static_reply(static_reply):
    for char in static_reply:
        print(char, end="", flush=True)
        time.sleep(0.01)  # Adjust the delay as needed
    print() 


device = "cuda" if torch.cuda.is_available() else "cpu"
print("Device: ", device)
logging.info(f"Device selected: {device}")

kArray=[5,2,1]

# Initialize global variable
model = None

# @profile
def load_model():
    #Loads the Ollama model if not already loaded
    global model
    if model is None:
        try:
            logging.info("Loading Ollama model: llama3:instruct...")
            torch.manual_seed(42)
            model = Ollama(model="llama3:instruct", temperature=0, keep_alive=-1)
            logging.info("Ollama model initialized successfully.")
        except Exception as e:
            logging.critical(f"Failed to initialize Ollama model: {e}")
            raise
            # model = ChatOllama(model="llama3:instruct", temperature=0, keep_alive=0, seed=42) #Ensures model is loaded only once
    else:
        logging.info(f"⚡ Model already loaded, reusing instance: {id(model)}")

# Load model at import
load_model()
    

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
    global db, db_tbl, embedding_function

    # Ensure embedding_function is loaded
    if 'embedding_function' not in globals():
        load_embedding()  # Load it if not already loaded
        
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
def query_rag(query_text, prompt_index, history):

    global model # Ensure we reference the global model

    context_text = ""

    if db is None or db_tbl is None:
        logging.error("Database objects are not initialized.")
        return ["Error: Database not loaded.", []]
    
    if model is None:
        logging.error("Model is not initialized. Call load_model() first.")
        return ["Error: Model not loaded.", []]

    if prompt_index == 0:
        dbt = db
    else:
        dbt = db_tbl

    logging.info(f"Query: {query_text}")
    try:
        future_results_tbl = executor.submit(dbt.similarity_search_with_score, query_text, k=kArray[prompt_index])
        logging.debug(f"Future results: {future_results_tbl}")
        results = future_results_tbl.result()
        logging.debug(f"Search results obtained: {len(results)} documents.")
    except Exception as e:
        logging.error(f"Error during similarity search: {e}")
        return ["Error during query processing.", []]
    
    context_text = build_context(results)

    if model is None:
        logging.error("❌ Model reference lost! Reloading...")
        load_model()  # Reload model if necessary
        if model is None:
            return ["Error: Model reloading failed.", []]

    # Build the chain
    try:
        prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE[prompt_index])
        chain = prompt | model | StrOutputParser()
        logging.info("Query chain created successfully.")
    except Exception as e:
        logging.error(f" Error while creating query chain: {e}")
        return ["Error during query processing.", []]

    # prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE[prompt_index])
    # chain = prompt | model | StrOutputParser()

    # Set up response generation
    stop_flag=threading.Event()
    future = executor.submit(run_chain, chain, query_text, history, stop_flag, context_text)

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

    logging.info(f"Final Response in query rag function: {response_text}")
    logging.info(f"Final Sources in query rag function: {sources}")

    return [response_text, sources]


def query(query_text, prompt_index, history=None, context=None):    

    logging.info(f"Running query with prompt index {prompt_index}")
    prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE[prompt_index])
    chain= prompt | model | StrOutputParser()

    stop_flag=threading.Event()
    future = executor.submit(run_chain, chain, query_text, history, stop_flag, context)

    while not future.done():
        if stop_loop:
            stop_flag.set()  # Signal the chain to stop
            print("\n\nStopping response generation...")
            logging.info("Stopping response generation...")

            break
        time.sleep(0.01)  # Check periodically

    # Wait for the response to complete if it hasn't already
    if future.done():
        logging.info("Fetching future.result() now...")
        response_text = future.result()
        logging.info(f"Received response: {response_text}")
    else:
        response_text = "Response generation was interrupted."

    sources = ["contextual"]
    logging.info(f"Response generated: {response_text[:100]}...")  # Log the first 100 characters

    logging.info(f"Final Response in query function: {response_text[:100]}")
    logging.info(f"Final Sources in query function: {sources}")

    return [response_text, sources]

def query_with_object_routing(query_text, prompt_index, history):
    logging.info(f"Received query: {query_text} with index {prompt_index}")

    # Classify the query object and extract context
    object_name, context = classify_query_object_category(model, query_text)
    print(f"Generating response for {object_name}")

    if object_name:
        if object_name == "WORK_CALENDAR":
            logging.info("Query matched with Work Calendar object.")
            
            # Extract country and year
            country, year = work_cal_country_extract(model, query_text)
            print("Country=", country, "\nYear=", year)

            if country is not None:
                holiday_list = get_or_update_work_cal(country, year)
                logging.info(f"Holiday list acquired for {country} in {year}: {holiday_list}")

                [response_text, sources] = query(query_text, 4, str(history), context)
                logging.info("IF 1 BLOCK 1 IF CALLED")
                logging.info(f"resssspnse partt 1:, {response_text[:100]}, {type(response_text)}")
                #history.append({"role": "assistant", "content": response_text[0], "sources": " "})
                
                [response_text2, sources] = query(query_text, 5, str(history), holiday_list)
                logging.info(f"resssspnse text 2, {response_text2[:100]}, {type(response_text)}")
                #history.append({"role": "assistant", "content": response_text2[0], "sources": " "})
                response_text += response_text2
                logging.info(f"IF 1 BLOCK 2 IF CALLED")
                logging.info(f"resssspnse parrt 2:, {response_text[:100]}, {type(response_text)}")
                return [response_text, sources]
            else:
                response_text = query(query_text, 2, str(history), context)
                logging.info(f"IF 1 BLOCK 1 ELSE CALLED")
                history.append({"role": "assistant", "content": response_text[0], "sources": " "})
                return response_text

        elif object_name == "TO_DO_TYPE":
            context1 = object_categories.to_do_type_1
            context2 = object_categories.to_do_type_2

            [response_text, sources] = query(query_text, 2, str(history), context1)
            logging.info(f"ELIF 1 BLOCK CALLED")
            logging.info(f"resssspnse partt 1:, {response_text[0][:100]}, {type(response_text[0])}")
            #history.append({"role": "assistant", "content": response_text[0], "sources": " "})
            
            [response_text2, sources] = query(query_text, 2, str(history), context2)
            logging.info(f"resssspnse text 2, {response_text2[:100]}, {type(response_text)}")
            response_text += response_text2
            logging.info(f"ELIF 2 BLOCK CALLED")
            logging.info(f"resssspnse parrt 2:, {response_text[:100]}, {type(response_text)}")
            #history.append({"role": "assistant", "content": response_text[0], "sources": " "})
            return [response_text, sources]

        elif object_name == "COUNTRY":
            country = extract_country_from_query(model, query_text)
            print("\nCountry: ", country)

            if country and country != "None":
                insert_ci_country, insert_ci_country_l = get_address_format_by_country_name_sheet(country)

                response_text = f"""Response: Here are the two SQL `INSERT` queries for country {country}:

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
                states_country = get_states_by_country_name_api(country)
                response_text += f"\n\nHere are the two SQL `INSERT` queries for the states in {country}:\n\n**CI_STATE**\n```sql\n{states_country[0]}```\n\n**CI_STATE_L**\n```sql\n{states_country[1]}```\n\nNumber of states in {country}: {states_country[2]}"

                stream_static_reply(response_text)
            else:
                response_text = query(query_text, 2, str(history), context)
                logging.info(f"AN ELSE BLOCK CALLED")
                return response_text

        else:
            response_text = query(query_text, 2, str(history), context)
            logging.info(f"ESLE BLOCK CALLED")
            return response_text
        logging.info(f"Response inside the else of function: {response_text[:100]}")
        history.append({"role": "assistant", "content": response_text[0], "sources": ""})

    else:
        print("Object not found.. resorting to RAG retrieval")
        response_text = query_rag(query_text, prompt_index, str(history))
        logging.info(f"QUERY RAG BLOCK CALLED")
        print("\nSources: ", response_text[1])
        history.append({"role": "assistant", "content": response_text[0], "sources": response_text[1]})

    sources = [" "]
    logging.info(f"Final Response: {response_text}")
    logging.info(f"Final Sources: {sources}")
    logging.info("REACHED HERE")
    return response_text




# Main Loop
if __name__ == "__main__":
    load_dotenv()

    api_key = os.getenv("CALENDARIFIC_API_KEY")

    if api_key:
        print(f" API Key Loaded Successfully: {api_key[:4]}****")
    else:
        print(" API Key Not Found! Check your .env file.")

    logging.info("Application started.")
    inp=""
    history=[]
    response=""
    chatY=0
    pfs=["C2M info","DB info","DB config help", "Country config"]
    
    
    load_model()
    load_embedding()
    load_faiss()

    print("Enter 'quit' to exit")
    print("Enter: \n pf0 for C2M info \n pf1 for DB info \n pf2 for DB config help \n\nDefault prompt template is C2M info")
    while(True):
        stop_loop = False
        inp=input("\nQuery: ")
        if(inp.lower()=="quit"):
            logging.info("Exiting application.")
            break
        if(inp.lower()=="pf0"or inp.lower()=="pf1" or inp.lower()=="pf2" or inp.lower()=="pf3"):
            ind=int(inp[-1])
            logging.info(f"Prompt Format selected: {pfs[ind]}")
            print("Prompt Format: ",pfs[ind])
            continue
        
        history.append({"role":"user","content":inp})
        try:
            object_name=""

            logging.info(f"Indice: {ind}")

            if ind==2:

                logging.info(f"Inside IF Indice: {ind}")
                
                object_name, context=classify_query_object_category(model, inp)
                print(f"Generating response for {object_name}")

                if object_name:
                    if object_name=="WORK_CALENDAR":
                        logging.info("Query matched with Work Calendar object.") 

                        #routing to prompt for work calendar 
                        country, year = work_cal_country_extract(model, inp)
                        print("Country=", country, "\nYear=", year)

                        if country!=None:
                            holiday_list=get_or_update_work_cal(country, year)
                            logging.info(f"Holiday list acquired for {country} in {year}: {holiday_list}") 
                            print(holiday_list)
                        
        
                            response = query(inp, 4, str(history))
                            history.append({"role": "assistant", "content": response[0], "sources": " "})
                            response = query(inp, 5, str(history), holiday_list)
                            history.append({"role": "assistant", "content": response[0], "sources": " "})
                        else:
                            response = query(inp, 2, str(history), context)
                            history.append({"role": "assistant", "content": response[0], "sources": " "})
                            
                    elif object_name=="TO_DO_TYPE":
                        context1=object_categories.to_do_type_1
                        context2=object_categories.to_do_type_2

                        response = query(inp, 2, str(history), context1)
                        history.append({"role": "assistant", "content": response[0], "sources": " "})
                        response = query(inp, 2, str(history), context2)
                        history.append({"role": "assistant", "content": response[0], "sources": " "})

                    elif object_name=="COUNTRY":
                        country=extract_country_from_query(model, inp)
                        print("\nCountry: ", country)
                        if country or country!="None":
                            insert_ci_country, insert_ci_country_l = get_address_format_by_country_name_sheet(country)
                            # response=query(inp, ind, str(history), address_format)
                            
                            #To be updated with a model that can provide accurate results for country config
                            response=f"""Response:  Here are the two SQL `INSERT` queries for country {country}:

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
                            states_country = get_states_by_country_name_api(country)
                            response+=f"Here are the two SQL `INSERT` queries for the states in country {country}:\n\n**CI_STATE**\n```sql\n{states_country[0]}```\n\n**CI_STATE_L**\n```sql\n{states_country[1]}```\n\nNumber of states in country {country}: {states_country[2]}"
                        
                            stream_static_reply(response)
                        else:
                            response = query(inp, 2, str(history), context)
                    else:
                        response = query(inp, 2, str(history), context)
                    history.append({"role":"assistant","content":response,"sources":""})
                    
                else:
                    print("Object not found.. resorting to RAG retreival") #Remove comment later
                    response=query_rag(inp, ind, str(history))
                    print("\nSources: ",response[1])
                    history.append({"role":"assistant","content":response[0],"sources":response[1]})

            else:
                response=query_rag(inp, ind, str(history))
                print("\nSources: ",response[1])
                history.append({"role":"assistant","content":response[0],"sources":response[1]})
        except Exception as e:
            logging.critical(f"Critical error in main loop: {e}")

        while True:
            if object_name!="COUNTRY":
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
    listener.stop() 
    executor.shutdown() 
    