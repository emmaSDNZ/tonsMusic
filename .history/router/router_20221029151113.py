from fastapi import APIRouter
from config.db import conn
from schema.user_schema import  UserSchema
from model.user import users



users = APIRouter()

@users.get('/')
def root():
    return {"message" : "Hi am fasApi from ROUTE"}

@users.post('/api/user')
def create_user( data_user: UserSchema ):
    new_user = data_user.dict()
    conn.execute(users.insert().values(new_user))

    return "success"