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
def getAllUsers():
    return conn.execute( users.select() ).fetchall()

@user.get('/api/user/{id}')
def getUserId( id: str):
    print(id)
    userId = conn.execute(users.select().where( users.c.id == id)).first()
    return userId

@user.delete('/api/user/{id}')
def deletUserId(id: str):
    deletId = conn.execute( users.delete().where(users.c.id == id)).first()
    return " {id} deleted"

@user.post('/api/user')
def create_user( data_user: UserSchema ):
    result=  conn.execute( users.insert().values( data_user.dict() ) )
    return conn.execute( users.select().where( users.c.id == result.lastrowid) ).first()

