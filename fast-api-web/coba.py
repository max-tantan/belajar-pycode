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

    if user.username in users:
        raise(HTTPException(status_code=400, detail="Username sudah digunakan"))
    
    hashed_password = hash_password(user.password)
    users[user.username] = hashed_password
    save_users(users)

#login endpoint
@app.post("/login")
def login(user: User):
    users = load_users()

    if user.username not in users:
        raise HTTPException(status_code=400, detail="Username tidak ditemukan")
    
    hashed_input_password = hash_password(user.password)
    stored_hashed_password = users[user.username]

    if hashed_input_password == stored_hashed_password:
        return {"message": "Login berhasil"}
    else:
        raise HTTPException(status_code=400, detail="Password salah")
    
    return {"message": f"selamat datang, {user.username}!"}