from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def home():
    return {'message':'AI Engineer API is running !'}


from pydantic import BaseModel
class ChatRequest(BaseModel):
    message:str
    
@app.post('/chat')
def chat(request:ChatRequest):
    return {'response':f'You said:{request.message}'}    





















from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()

@app.get('/')
def home():
    return {'message':'Hello Ahmed , I am your AI assistant'}


class ChatRequest(BaseModel):
    message:str
    
@app.post('/chat')
def chat(request:ChatRequest):
    return {'response':f'You said : {request.message}'}



    