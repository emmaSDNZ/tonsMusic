from fastapi import FastAPI
from router.router import users


app = FastAPI()

app.include_router(users)