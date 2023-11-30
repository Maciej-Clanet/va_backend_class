from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List


from db.dbutils import generateUuid
from db.userUtils import getUsers, saveUsers
from db.profilesUtils import createProfile, getProfileById, saveProfileChange

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

    #create profile for the user
    createProfile(new_user["id"])

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



class ProfileData(BaseModel):
    user_id: str
    bio: str
    art_categories: List[str]
    product_categories: List[str]

@router.post("/profile", response_model=ProfileData)
async def getProfile(profileRequest: UserId):
    profile = getProfileById(profileRequest.id)
    if(not profile):
       raise HTTPException(400, detail="Could not get profile data")
    
    return profile


class UpdateProfile(BaseModel):
    user_id: str
    bio: str = None
    art_categories: List[str] = None
    product_categories: List[str] = None 

@router.post("/updateprofile")
async def updateProfile(newData: UpdateProfile):
    
    oldProfile = getProfileById(newData.user_id)
    
    if newData.bio is not None:
        oldProfile["bio"] = newData.bio
    if newData.art_categories is not None:
        oldProfile["art_categories"] = newData.art_categories
    if newData.product_categories is not None:
        oldProfile["product_categories"] = newData.product_categories

    saveProfileChange(newData.user_id, oldProfile)

    
