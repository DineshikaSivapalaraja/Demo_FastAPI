from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
async def hello():
    return "hello"