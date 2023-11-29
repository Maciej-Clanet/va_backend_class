from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/test")
async def test():
    return {"message" : "users endpoint works"}