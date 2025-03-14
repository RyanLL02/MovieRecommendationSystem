from fastapi import FastAPI
from database import init_db
from routes import movie

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

app.include_router(movie.router)

@app.get("/")
def read_root():
    return {"message": "Movie Recommendation API Running"}