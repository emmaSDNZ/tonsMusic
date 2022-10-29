from fastapi import APIRouter
from schema.user_schema import  UserSchema
from config.db import conn
from model.user import users


user = APIRouter()

@user.get('/')
def root():
    return {"message" : "Hi am fasApi from ROUTE"}

@user.post('/api/user')
def create_user( data_user: UserSchema ):
    print(data_user)