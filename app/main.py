from fastapi import FastAPI
from api.endpoints import users


app = FastAPI(
    title="GameShop",
    version="1.0",
)


app.include_router(users.router)