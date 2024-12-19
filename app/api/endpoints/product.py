from fastapi.routing import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel
from DB import database
from bson import json_util
import json
from typing import Union
from bson import ObjectId
from boto3 import session
from typing import Annotated
from fastapi import File, UploadFile, Form


ACCESS_ID = 'DO801R8K4EMW2KYRRLYC'
SECRET_KEY = 'au3xVZScp+DifTMt5qM+MsQy2aB8yfqUPX6grUdKYug'

session = session.Session()
client = session.client('s3',
                        region_name='nyc3',
                        endpoint_url='https://nyc3.digitaloceanspaces.com',
                        aws_access_key_id=ACCESS_ID,
                        aws_secret_access_key=SECRET_KEY)


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
    catagory: str
    key_features: str
    brand_name: str
    description: str

@router.post("/add_product")
async def add_product(product: Product):  # Expect a Product model instance
    try:
        print(product)
        product_data = product.model_dump()
        DB = database.MongoDB(DB_URL, DB_NAME)
        DB.insert_one("products", product_data)
        return {"message": "Product added successfully!", "product": product_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

class Order(BaseModel):
    address: str
    quantity: str
    prioduct_id: str
    phoneNumber: str
    userid: str

@router.post("/add_order")
async def add_order(order: Order):
    try:
        data = order.model_dump()
        print(data)
        DB = database.MongoDB(DB_URL, DB_NAME)
        DB.insert_one("orders", data)
        return {"message": "Order added successfully!", "order": data}
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

@router.post("/upload_image")
async def upload_image(file: Annotated[UploadFile, Form(...)]):
        try:
            contents = await file.read()
            content_type = file.content_type

            client.put_object(
                Body=contents,
                Bucket='thesis-gamestopre',  # Your DigitalOcean Space name
                Key=file.filename,  # Name of the file to store in Spaces
                ACL='public-read',  # Make the file publicly accessible
                ContentType=content_type  # Set the correct content type for the file
            )
            return {"message": "Image uploaded successfully!"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))