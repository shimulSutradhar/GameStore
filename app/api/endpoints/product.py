from fastapi.routing import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel
from DB import database
from bson import json_util
import json
from typing import Union
from bson import ObjectId

DB_URL = "mongodb+srv://shimulsutradhar814:8GdKJHmXjAiwadvv@cluster0.g81ls.mongodb.net/"
DB_NAME = "gamestore"

router = APIRouter()

@router.get("/amra")
async def send_thank_you():
    return {"message": "Thank you!"}

class Product(BaseModel):
    name: str
    price: int
    image: str
    catagory: list[str]
    key_features: list[str]
    brand_name: str
    description: str

@router.post("/add_product")
async def add_product(product: Product):
    try:
        print(product)
        DB = database.MongoDB(DB_URL, DB_NAME)
        DB.insert_one("products", product.model_dump())
        return {"message": "Product added successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_product")
async def get_product():
    try:
        DB = database.MongoDB(DB_URL, DB_NAME)
        products = DB.find_all("products", {})
        products_list = json.loads(json_util.dumps(products))
        print(products_list)
        return {"products": products_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class FildInfo(BaseModel):
    key: str
    value: Union[str, int]

@router.put("/update_product/{product_id}")
async def update_product(product_id: str, fildInfo: FildInfo):
    try:
        print("Checking model: ", fildInfo.key, fildInfo.value)
        DB = database.MongoDB(DB_URL, DB_NAME)
        update_result = DB.update_one(
            "products", 
            {"_id":  ObjectId(product_id)}, 
            {fildInfo.key : fildInfo.value}
        )
        print("Checking update result: ", update_result)
        if update_result > 0:
            return {"message": "Product updated successfully!"}
        else:
            raise HTTPException(status_code=404, detail="Product not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))