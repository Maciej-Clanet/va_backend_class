from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api import users, art

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

orgins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:3000",
    "https://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=orgins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(users.router, prefix="/users", tags=["Users"] )
app.include_router(art.router, prefix="/art", tags=["Art"])


@app.get("/")
async def root():
    return {"message" : "it works!"}