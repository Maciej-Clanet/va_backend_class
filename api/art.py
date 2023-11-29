from fastapi import APIRouter
from pydantic import BaseModel

from db.artworksUtils import getArtworks

router = APIRouter()


class NewArtworkRequest(BaseModel):
    amount: int = 6

@router.post("/newest")
async def newest_artworks(request: NewArtworkRequest):
    # artworks = getLatestArtworks(request.amount)
    artworks = getArtworks()

    sorted_artworks = sorted(artworks["artworks"], key=lambda art: art["created_at"], reverse=True )

    return sorted_artworks[:min(request.amount, len(sorted_artworks))]

