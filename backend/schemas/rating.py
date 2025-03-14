from pydantic import BaseModel

class RatingBase(BaseModel):
    user_id: int
    movie_id: int
    rating: float

class RatingCreate(RatingBase):
    pass

class RatingResponse(RatingBase):
    id: int

    class Config:
        from_attributes = True