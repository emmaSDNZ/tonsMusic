from fastapi import APIRouter
from config.db import conn
from schema.user_schema import  UserSchema
from model.user import users
from sqlalchemy import insert


user = APIRouter()

@user.get('/')
def root():
    return conn.execute(users.select()).fetch_all()

@user.post('/api/user')
def create_user( data_user: UserSchema ):
    conn.execute(users.insert().values(data_user.dict()))
    

    return "success"