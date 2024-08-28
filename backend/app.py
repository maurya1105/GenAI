from flask import Flask, request, jsonify,redirect,render_template,Response
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, send, emit
import copy
import requests
from datetime import datetime 
import threading
import time
import os

#Change query function here
from query_data_dummy  import query_rag

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
    [response,sources]=(query_rag(data["query"],str(data["history"]),int(data["chatType"])))

    user["response"]=response[:9] + "..."
    user["request"]="completed"
    log={"query":data["query"],"response":response,"reference":sources,"time":str(datetime.now()-dtime)}
    LOGS.append(f"{curtime} | [QRY] | user {ipadress} @ {user['agent']} | {log}")
    emit("response",{"response":response,"query":data["query"],"reference":sources,"chatIndex":data["chatIndex"]},broadcast=False)

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
    socketio.run(app,host="0.0.0.0")



