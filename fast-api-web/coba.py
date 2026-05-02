from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
from pathlib import Path
import json
import hashlib

app = FastAPI()
SECRET_KEY = "secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
USERS_FILE = Path(__file__).with_name("users.json")
security = HTTPBearer()

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalid")

#modal request
class User(BaseModel):
    username: str
    password: str

#helper
def load_users():
    try: 
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def save_users(users):
    with open(USERS_FILE, "w") as file:
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
    return {"message": "User berhasil dibuat"}

#login endpoint
@app.post("/login")
def login(user: User):
    users = load_users()

    if user.username not in users:
        raise HTTPException(status_code=400, detail="Username tidak ditemukan")
    
    if users[user.username] != hash_password(user.password):
        raise HTTPException(status_code=400, detail="Password salah")

    token = create_access_token({"sub": user.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

#protected endpoint
@app.get("/profile")
def profile(payload: dict = Depends(verify_token)):
    return {
        "message": "Token valid",
        "username": payload.get("sub")
    }
