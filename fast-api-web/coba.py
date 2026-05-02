from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import hashlib

app = FastAPI()

#modal request
class User(BaseModel):
    username: str
    password: str

#helper
def load_users():
    try: 
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#register endpoint
@app.post("/register")
def register(user: User):
    users = load_users()

    if user.username in usaers:
        raise(HTTPException(status_code=400, detail="Username sudah digunakan"))
    
