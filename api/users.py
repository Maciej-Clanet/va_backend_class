from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List


from db.dbutils import generateUuid
from db.userUtils import getUsers
# from db.userUtils import getUsers, saveUsers
# from db.profilesUtils import createProfile, getProfileById, saveProfileChange

router = APIRouter()


#AuthCredObject
class AuthCredentials(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    id: str
    username: str

#userIdObject
#ProfileDataObject
#UpdateProfile details object

#login


#register
@router.post("/register", response_model=LoginResponse)
async def register(credentials: AuthCredentials):
    usersJSON = getUsers()

    #check if user exists
    for user in usersJSON["users"]:
        if(credentials["email"] == user["email"])
            raise HTTPException(400, )


    

#profile

#update profile

    
