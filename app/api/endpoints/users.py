from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from DB import database
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
    return {"message": "User created successfully", "user": user}

@router.get("/users")
async def get_users():
    DB = database.MongoDB(DB_URL, DB_NAME)
    users = DB.find_all("users", {})
    for i in users:
        print(i)
    return {"users": "users"}