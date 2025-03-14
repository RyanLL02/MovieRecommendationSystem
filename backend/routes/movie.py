from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.movie import Movie
from schemas.movie import MovieCreate, MovieResponse

router = APIRouter(prefix="/movies", tags=["movies"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=MovieResponse)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    new_movie = Movie(title=movie.title, genre=movie.genre, description=movie.description)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie