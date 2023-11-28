from fastapi import fastapi
from fastapi.moiddleware.cors import CORSMiddleware


app = FastAPI()

orgins = [
    "http://localhost",
    "https://localhost",
    "http://localhost:3000",
    "https://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origns=orgins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def root():
    return {"message" : "it works!"}