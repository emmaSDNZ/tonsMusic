from fastapi import APIRouter

user = APIRouter()

@user.get('/')
def root():
    return {"message" : "Hi am fasApi from ROUTE"}

@user.post('/api/user')
def create_user( data_user ):
    pass