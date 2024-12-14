from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from DB import database
from bson import json_util
import json

DB_URL = "mongodb+srv://shimulsutradhar814:8GdKJHmXjAiwadvv@cluster0.g81ls.mongodb.net/"
DB_NAME = "gamestore"

router = APIRouter()

class CreateUserRequest(BaseModel):
    name: str
    email: str
    password: str

@router.get("/")
async def send_thank_you():
    return {"message": "Thank you!"}

@router.post("/create_user")
async def create_user(user: CreateUserRequest):
    DB = database.MongoDB(DB_URL, DB_NAME)
    DB.insert_one("users", user.model_dump())
    return {"message": "User created successfully"}

@router.get("/users")
async def get_users():
    DB = database.MongoDB(DB_URL, DB_NAME)
    users = DB.find_all("users", {})
    
    users = json.loads(json_util.dumps(users))
    for user in users:
        user.pop('_id', None)
    return users

class VerifyUserRequest(BaseModel):
    email: str
    password: str

@router.post("/verify_user")
async def verify_user(user: VerifyUserRequest):
    DB = database.MongoDB(DB_URL, DB_NAME)
    existing_user = DB.find_one("users", {"email": user.email, "password": user.password})
        
    if existing_user:
        return {"message": "User verified successfully"}
    else:
        raise HTTPException(status_code=401, detail="Invalid email or password")