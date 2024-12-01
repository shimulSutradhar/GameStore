from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

@router.get("/")
async def send_thank_you():
    return {"message": "Thank you!"}

@router.post("/create_user")
async def create_user(user: CreateUserRequest):
    # Here you would normally add the user to the database
    # For now, we'll just return the user data
    print(user)
    return {"message": "User created successfully", "user": user}