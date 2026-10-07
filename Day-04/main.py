def add(a:int,b:int)->int:
    return a+b

def greet(name:str)->str:
    return f"Hello {name}"

def get_names()->list[str]:
    return ['Ahmed','Ali','Omar']



from pydantic import BaseModel
import os

class chatRequest(BaseModel):
    message:str
    temperature:float

def create_prompt(request:chatRequest)->str:
    return f"User Prompt : {request.message}"


api_key=os.getenv("MY_API_KEY")

request=chatRequest(message="Explain Neural Networks",temperature=0.7)

prompt=create_prompt(request)

print(prompt)
print(f"API Key exists : {api_key is not None}")
        