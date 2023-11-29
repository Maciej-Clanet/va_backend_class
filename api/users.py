from fastapi import APIRouter
from pydantic import BaseModel

from db.dbutils import *

router = APIRouter()

@router.get("/test")
async def test():
    # return getUserById("06a990750bfe40069041d66322da8511")
    # return getUsers()
    # return addUser("test", "test@gmail.com", "1234")
    # addProduct(1, "testcat", "title", "description", 3.50, "image url")
    # return getProductsByUser(1)
    temp = ["tag1", "tag2"]
    addArtwork(generateUuid(), "test category", "test title", "test desc", "image", temp)
    return getArtworks()
    # return getArtworksByUser(1)
    # return getLatestArtworks(2)