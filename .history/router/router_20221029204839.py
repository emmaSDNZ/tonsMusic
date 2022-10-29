from fastapi import APIRouter, Response, status
from config.db import conn
from schema.user_schema import  UserSchema
from model.user import users
from starlette.status import HTTP_204_NO_CONTENT


user = APIRouter()

@user.get('/')
def root():
    return {
        "message" : "ApiRest disqueria",
        "version": "1.0.0",
        "satus": True,
        }

@user.get('/api/user', response_model=list[UserSchema] )
def getAllUsers():
    return conn.execute( users.select() ).fetchall()

@user.get('/api/user/{id}', response_model=UserSchema)
def getUserId( id: str):
    print(id)
    userId = conn.execute(users.select().where( users.c.id == id)).first()
    return userId

@user.delete('/api/user/{id}', status_code=status.HTTP_204_NO_CONTENT)
def deleteUserId(id: str):
    conn.execute( users.delete().where(users.c.id == id))
    return Response(status_code= HTTP_204_NO_CONTENT )

@user.put('/api/user/{id}', response_model=UserSchema)
def putUserId(id: str, user: UserSchema):
    conn.execute( users.update().values( name= user.name, username= user.username ).where(users.c.id == id))
    updateUserId =  conn.execute(users.select().where( users.c.id == id)).first()
    return updateUserId

@user.post('/api/user', response_model=UserSchema)
def create_user( data_user: UserSchema ):
    result=  conn.execute( users.insert().values( data_user.dict() ) )
    return conn.execute( users.select().where( users.c.id == result.lastrowid) ).first()

