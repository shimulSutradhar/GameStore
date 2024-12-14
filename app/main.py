from fastapi import FastAPI
from api.endpoints import users, product


app = FastAPI(
    title="GameShop",
    version="1.0",
)


app.include_router(users.router)
app.include_router(product.router)