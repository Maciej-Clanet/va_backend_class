from fastapi import APIRouter
from pydantic import BaseModel

from db.dbutils import *

router = APIRouter()


class NewArtworkRequest(BaseModel):
    amount: int = 6

@router.post("/newest")
async def newest_artworks(request: NewArtworkRequest):
    artworks = getLatestArtworks(request.amount)
    return artworks
