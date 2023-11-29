from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from db.dbutils import generateUuid
from db.userUtils import getUsers, saveUsers

router = APIRouter()

class AuthCredentials(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    id: str
    username: str

class UserId(BaseModel):
    id : str

@router.post("/register", response_model=LoginResponse)
async def register(credentials: AuthCredentials):
    print(credentials)
    #make sure email wasn't used before
    users = getUsers()
    for user in users["users"]:
        if(user["email"] == credentials.email):
            raise HTTPException(400, detail="account already exists")
    
    #doesn't exist, create one
    username = credentials.email.split("@")[0]
    new_user = {
        "id": generateUuid(),
        "email" : credentials.email,
        "username": username,
        "password": credentials.password
    }
    users["users"].append(new_user)
    saveUsers(users)

    return {"id": new_user["id"], "username" : new_user["username"]}


@router.post("/login", response_model=LoginResponse)
async def login(credentials: AuthCredentials):
    users = getUsers()["users"]
    for user in users:
        if(user["email"] == credentials.email):
            #user exist check password
            if(user["password"] == credentials.password):
                #correct
                return {"id": user["id"], "username" : user["username"]}
            else:
                #wrong password
                raise HTTPException(400, detail="incorrect password")

    #user not found
    raise HTTPException(400, detail="user not found")



@router.post("/profile")
async def getProfile(id: UserId):
    pass


