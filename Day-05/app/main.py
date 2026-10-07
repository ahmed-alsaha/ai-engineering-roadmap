from fastapi import FastAPI
import asyncio

app=FastAPI()

@app.get("/")
async def hello():
    await asyncio.sleep(2)
    return {"message":"Hello from async API"}