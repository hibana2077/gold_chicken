from fastapi import FastAPI
import uvicorn
import redis
import os

API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = os.getenv("API_PORT", 8081)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

redis_counter_db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0) # Redis DB for counter
redis_user_db = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=1) # Redis DB for user

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/login")
def login(data: dict):
    username = data.get("username")
    password = data.get("password")
    if redis_user_db.get(username) == password:
        return {"status": "success"}
    return {"status": "failed"}

@app.post("/change_password")
def change_password(data: dict):
    username = data.get("username")
    old_password = data.get("old_password")
    new_password = data.get("new_password")
    if redis_user_db.get(username) == old_password:
        redis_user_db.set(username, new_password)
        return {"status": "success"}
    return {"status": "failed"}

if __name__ == "__main__":
    uvicorn.run(app, host=API_HOST, port=API_PORT)