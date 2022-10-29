from fastapi import APIRouter
from config.db import conn
from schema.user_schema import  UserSchema
from model.user import users
from sqlalchemy import insert


user = APIRouter()

@users.get('/')
def root():
    return {"message" : "Hi am fasApi from ROUTE"}

@users.post('/api/user')
def create_user( data_user: UserSchema ):
    result = conn.execute(users.insert().values(data_user.dict()))
    print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    print(result)

    return "success"