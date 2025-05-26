import os
import uvicorn

if __name__ == "__main__":

    try:
       uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    except Exception as e:
        print(f"Error starting the server: {e}")
        os.system("python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload")


   
            
            
