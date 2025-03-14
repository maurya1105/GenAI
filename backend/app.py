from flask import Flask, request, jsonify,redirect,render_template,Response
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, send, emit
import copy
import requests
from datetime import datetime 
import threading
import time
import os

import logging

# Create a logger for app.py
app_logger = logging.getLogger("app_logger")
app_logger.setLevel(logging.INFO)

# Create a file handler for app.py
app_handler = logging.FileHandler("app_py_logs.log")  # Log file for app.py
app_handler.setLevel(logging.INFO)

# Set formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
app_handler.setFormatter(formatter)

# Add handler to logger
app_logger.addHandler(app_handler)

# Prevent duplicate logs
app_logger.propagate = False

# Example log entry
app_logger.info("Server started now")


from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check if the API key is loaded
api_key = os.getenv("CALENDARIFIC_API_KEY")

if api_key:
    print(f"✅ API Key Loaded Successfully: {api_key[:4]}****")
else:
    print("❌ API Key Not Found! Check your .env file.")

#Change query function here
#from query_faiss import query_rag
from chatbot_2 import query_rag, load_faiss, query_with_object_routing

# Ensure FAISS indices are loaded before accessing `db_tbl`
load_faiss()

app = Flask(__name__)
cors=CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = 'secret!'
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
uform={"ip":None,"agent":None,"status":None,"request":None,"query":None,"response":None,"current time":0,"total time":0,"disconnected":0}
users=[]
CORS(app,resources={r"/*":{"origins":"*"}})
socketio = SocketIO(app,cors_allowed_origins="*")

#Also change query function here
#To load the model into memory
time1=datetime.now()
query_rag("Start","",0)
print("Start up time: ",datetime.now()-time1)
time.sleep(2)
spc="            "
LOGS=["\n"+"-x"*25 + "-","\n"+datetime.now().strftime("%Y-%m-%d %H:%M:%S")+" | Server started","="*50," "*21+"LOGS"+" "*20,"="*50]

def get_Loc(ip):
    response = requests.get("https://ipgeolocation.abstractapi.com/v1/?api_key=[api-key]&ip_address="+ip)
    return " "

@socketio.on("connect")
def connected():
    ipadress=request.remote_addr
    user=None
    if ipadress not in [user["ip"] for user in users]:
        user=copy.deepcopy(uform)
        user["ip"]=ipadress
        uagent=request.headers.get('User-Agent')
        uagent=uagent[uagent.find(";")+1:uagent.find(")")]
        user["agent"]=uagent[:uagent.find(";")]
        user["status"]="connected"
        users.append(user)
        
    else:
        user=[user for user in users if user["ip"]==ipadress][0]
        user["status"]="connected"
        user["disconnected"]=0
        user["request"]=None
        user["query"]=None
        user["response"]=None
        user["current time"]=0
    curtime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    LOGS.append(f"{curtime} | [CON] | user {ipadress} @ {user['agent']}")


@socketio.on("query")
def message(data):
    ipadress=request.remote_addr
    dtime=datetime.now()
    curtime=dtime.strftime("%Y-%m-%d %H:%M:%S")
    
    user=[user for user in users if user["ip"]==ipadress][0]
    
    user["request"]="querying"
    user["query"]=data["query"] if len(data["query"])<13 else data["query"][:9]+"..." 

    #Also change query function here

    if int(data["chatType"]) == 2:
        [response,sources]=(query_with_object_routing(data["query"],int(data["chatType"]),str(data["history"])))
        app_logger.info(f"Response received in app.py: {response}")
        app_logger.info(f"Sources received in app.py: {sources}")
    else:
        [response,sources]=(query_rag(data["query"],int(data["chatType"]),str(data["history"])))
        app_logger.info(f"Response of query rag received in app.py: {response}")
        app_logger.info(f"Sources of query rag received in app.py: {sources}")

    user["response"]=response[:9] + "..."
    user["request"]="completed"
    log={"query":data["query"],"response":response,"reference":sources,"time":str(datetime.now()-dtime)}
    LOGS.append(f"{curtime} | [QRY] | user {ipadress} @ {user['agent']} | {log}")
    emit("response",{"response":response,"query":data["query"],"reference":sources,"chatIndex":data["chatIndex"]},broadcast=False)
    app_logger.info("Emitting response to frontend.")


@socketio.on("disconnect")
def disconnected():
    ipadress=request.remote_addr
    user=[user for user in users if user["ip"]==ipadress][0]
    user["status"]="disconnected"
    curtime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    LOGS.append(f"{curtime} | [DIS] | user {ipadress} @ {user['agent']}")
    emit("disconnect",f"user {request.sid} disconnected",broadcast=False)


ord=list(uform.keys())
len_ord=len(ord)    
bar="  |  "
header=f"  User IP   {bar}User Agent  {bar}Status      {bar}Process     {bar}Query       {bar}Response    {bar}Current Time{bar}Total Time  "
def display():
    cls()
    while (True):
        cls()
        print("\033[0;0H"+header)
        print("─"*len(header))
        skipped=0
        for i in range(len(users)):
            if (users[i]["status"]=="disconnected" and users[i]["disconnected"]>4):
                skipped+=1
                continue
            for j in range(len_ord-1):
                z=" |  " if j>0 else ""
                print(f"\033[{i+3-skipped};{j*17-3}H{z}{users[i][ord[j]]}")
            if (users[i]["query"]!=None and users[i]["response"]==None):
                users[i]["current time"]+=1
                users[i]["total time"]+=1
            if (users[i]["status"]=="disconnected"):
                users[i]["disconnected"]+=1
        for log in LOGS:
            print(log)  
        time.sleep(1)

def logger():
    global LOGS
    logFile = open("user-activity.log", "a")
    while (True):
        
        for log in LOGS:
            logFile.write(log+"\n")
        logFile.flush()
        os.fsync(logFile.fileno())
        LOGS=[]
        time.sleep(1)
        

@app.route('/login', methods=['GET'])
def login():
 return 'hey'   

t1=threading.Thread(target=display)
t2=threading.Thread(target=logger)
t1.daemon=True
t2.daemon=True
t2.start()
t1.start()
if (__name__ == '__main__'):
    socketio.run(app,host="0.0.0.0", port=5000, allow_unsafe_werkzeug=True, use_reloader=False)



