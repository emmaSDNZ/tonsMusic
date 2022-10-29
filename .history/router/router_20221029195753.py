from fastapi import APIRouter
from config.db import conn
from schema.user_schema import  UserSchema
from model.user import users
from sqlalchemy import insert


user = APIRouter()

@user.get('/')
def root():
    return {
        "message" : "ApiRest disqueria",
        "version": "1.0.0",
        "satus": True,
        }

@user.get('/api/user')
def root():
    return conn.execute(users.select()).fetchall()

@user.post('/api/user')
def create_user( data_user: UserSchema ):
    result=  conn.execute(users.insert().values(data_user.dict()))
    print(result.lastrowid)
    return conn.execute(users.select().where(users.c.id == result.lastrowid))