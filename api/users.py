from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List


from db.dbutils import generateUuid
from db.userUtils import getUsers, saveUsers
from db.profilesUtils import getProfileById

router = APIRouter()


#AuthCredObject
class AuthCredentials(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    id: str
    username: str



#login
@router.post("/login", response_model=LoginResponse)
async def login(credentials: AuthCredentials):
    usersJSON = getUsers()
    #check if user exists
    for user in usersJSON["users"]:
        if(credentials.email == user["email"]):
            #user exists, check if password is correct
            if(credentials.password == user["password"]):
                return {"id" : user["id"], "username" : user["username"]}
            else:
                raise HTTPException(400, detail="wrong password")

    raise HTTPException(400, detail="user not found")

#register
@router.post("/register", response_model=LoginResponse)
async def register(credentials: AuthCredentials):
    usersJSON = getUsers()

    #check if user exists
    for user in usersJSON["users"]:
        if(credentials.email == user["email"]):
            raise HTTPException(400, detail="account already exists")

    #account doesn't exist, create one
    new_user = {
        "id": generateUuid(),
        "email" : credentials.email,
        "password" : credentials.password,
        "username" : credentials.email.split("@")[0]
    }

    usersJSON["users"].append(new_user)
    saveUsers(usersJSON)

    return {"id" : new_user["id"], "username" : new_user["username"]}
    

class UserIdObject(BaseModel):
    user_id: str

class ProfileData(BaseModel):
    bio: str
    profession: str
    art_categories: List[str]
    product_categories: List[str]

@router.post("/profile", response_model=ProfileData)
async def profile(id:UserIdObject):
    profile = getProfileById(id.user_id)

    if not profile:
        raise HTTPException(400, detail="no profile found")

    return profile


class UpdateProfileObject(BaseModel):
    user_id: str
    profession: str = None
    bio: str = None
    art_categories : List[str] = None
    product_categories : List[str] = None

#UpdateProfile details object
@router.post("/UpdatProfile")
async def updateProfileEndpoint(newData: UpdateProfileObject):
    currentProfile = getProfileById(newData.user_id)

    if newData.bio is not None:
        currentProfile["bio"] = newData.bio
    if newData.profession is not None:
        currentProfile["profession"] = newData.profession
    if newData.art_categories is not None:
        currentProfile["art_categories"] = newData.art_categories
    if newData.product_categories is not None:
        currentProfile["product_categories"] = newData.product_categories

    print(currentProfile)

















#UpdateProfile details object
## define the data, make every profile attribute optional except the id

#update profile
## the endpoint will acept UpdateProfile data
## get current profile state based on the id
## for every property that has been given by the frontend, overwrite the old profile value with the new
## save the profile change
    
