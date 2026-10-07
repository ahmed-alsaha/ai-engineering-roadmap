from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI(title='Mni ChatGPT API')

class PromptRequest(BaseModel):
    prompt:str

@app.get("/")
def home():
    return {"message":"Welcome to Mini ChatGPT API !"}

@app.post("/generate")
def generate_response(request:PromptRequest):
    dummy_response=f"Echo response to : '{request.prompt}'"
    return {
        "status":"success",
        "input_prompt":request.prompt,
        "response":dummy_response
    }    