
___
<br/>
<br/>
<span style="font-size:35px; font-weight:500;color:white">Getting Started</span>
<br/>
<br/>
<br/>

# 
<br/>
<br/>

<span style="font-size:30px; font-weight:500;color:white">Backend:</span>
<br/>
<br/>

- <span style="font-size:25px; font-weight:500;color:white">Setting Up</span>  <span style="font-size:12px;color:red">(Linux preferred as query time is drastically shorter.)</span>.
    - ### Install [Nvidia Drivers](https://www.nvidia.com/download/index.aspx)
    
    - ### Install [Cuda](https://developer.nvidia.com/cuda-downloads)
    
    - ### Install Python 3.11.2 (3.10+ should work)
    
    - ### Install [Pytorch](https://pytorch.org/get-started/locally/) (I used:  Stable (2.3.1) - Linux - Pip - Python - Cuda12.1)
   
        #### Ensure Cuda is working by running 
        ```
        python
        import torch
        torch.cuda.is_available()
        #[it should return "True" here]
        quit()
        ```
        #### It should return `True`
    
    - ### Continue installing dependencies

        Run
        ```
        pip install flask==3.0.3 flask_cors==4.0.1 flask_socketio==5.3.6 langchain_community==0.2.5 langchain_huggingface==0.0.3 
        ```
    
        - On Linux with GPU
            ```
            pip install faiss-gpu-cuXX
            ```

     
            (Replace XX with your CUDA version, here  I used `faiss-gpu-cu12==1.8.0.1` )


     
        - On Windows/no CUDA
            ```
            pip install faiss-cpu
            ```
    
    - ### Download & install [Ollama](https://ollama.com/download)
        Run
        ```
        ollama pull mistral
        ```
- <span style="font-size:25px; font-weight:500;color:white">Start</span>

    Run

    ```
    cd backend
    flask run --host=0.0.0.0
    ```
<br/>

---
<br/>
<br/>
<span style="font-size:30px; font-weight:500;color:white">Frontend:</span>
<br/>
<br/>
<br/>

-  <span style="font-size:25px; font-weight:500;color:white">Setting Up</span>

    - ### Ensure [npm](https://nodejs.org/en/download/package-manager) is installed (I used: node-v18.19.0, npm-9.2.0)
    - ### Install dependencies
        ```
        cd frontend
        npm i
        ```
    - ### Set socket url
        In `frontend` > `src` > `Constants.jsx`
        
        Set const URL to 

        `
        http://[--backendIP--]:5000
        `

        Use localhost if running on the same device as backend (`http://localhost:5000`)
        
        Use local ip if on same network as backend (get backend ip by using ` hostname -I` )

        Use global/public ip if backend is hosted (get backend ip by using `curl ifconfig.me`)
-  <span style="font-size:25px; font-weight:500;color:white">Start</span>
    
    Run

    ```
    cd frontend
    npx vite --host
    ```
    During development replace
    `npx vite --host` with `npm run dev`

<br/>

---