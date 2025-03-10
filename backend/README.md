# RAG-Model
Implementing a rag model that populates a database with documents that the finetuned LLM can build its context on. 

Can read multiple inputs like pdf, csv, txt and even schema from a database. Add those documents to a folder called 'data'.

1. **Install Python 3.X (3.10+ should work)**
   
2. **Install Nvidia drivers, Cuda, CudaCNN** and according to the version install **pytorch** from https://pytorch.org/get-started/locally/
   Skip this step for MacOS.

3. **Install Ollama** (https://ollama.com/download) and execute these commands:
  
   ```sh
   ollama pull llama3:instruct 
   ollama serve 
   ollama run llama3:instruct  
   ```
   
   To implement seed functionality in model:
   ```sh
   wget https://raw.githubusercontent.com/langchain-ai/langchain/master/libs/partners/ollama/langchain_ollama/chat_models.py -O .venv/lib/python3.11/site-packages/langchain_ollama/chat_models.py 
   ```
   **Ensure path is correctly set
   
4. **Clone/Pull repo** - LLM RAG pipeline- https://github.com/alfiyaanware/RAG-Model
   
5. **Install Python Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

    Only Linux supports faiss-gpu
   
    For MacOS or windows try:
    ```sh
    pip install faiss
    pip install faiss-cpu
    ```
   
6. **Enable Google Auth API key**:

   decrypt the data.json.gpg file using the command below:
   ```sh
    gpg -d data.json.gpg > data.json
   ```
   Use password shared with you by owner.

7. (Optional) **Oracle Client connection**:
   
   use extract4.py for data extraction from db schema using oracle connector
   
     a. Install Oracle Instant Client:
         - Download the Oracle Instant Client for macOS from the [Oracle website](https://www.oracle.com/in/database/technologies/instant-client/downloads.html).
         - Extract the files and move them to a directory (e.g., `/usr/local/oracle/instantclient_XX_X`).
     
     b. Set Up Environment Variables:
         ```sh
         export PATH=/usr/local/oracle/instantclient_19_8:$PATH
         export DYLD_LIBRARY_PATH=/usr/local/oracle/instantclient_19_8:$DYLD_LIBRARY_PATH
         ```
   once schema description is generated -> add file to data folder

8. **Run the project**:\
   
   -->Using the chatbot..
     ```sh
     python chatbot2.py
     ```

     
   -->Recreating faiss db
     ```sh
     python pop_db_faiss.py --reset (for resetting database) 
     
     python pop_db_faiss.py –add-new (for adding new docs to existing db) 
     ```
     delete existing faiss table index and use 
     ```sh
     python pop_db_faiss.py -–add-new-tbl (for adding new tbl info)
     ```
   
   






 
