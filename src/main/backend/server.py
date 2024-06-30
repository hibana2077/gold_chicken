from fastapi import FastAPI
import uvicorn
import redis
import os

API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = os.getenv("API_PORT", 8081)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

redis_counter_db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0) # Redis DB for counter

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host=API_HOST, port=API_PORT)