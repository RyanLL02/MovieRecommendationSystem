from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    genre: str
    description: str

class MovieCreate(MovieBase):
    pass

class MovieResponse(MovieBase):
    id: int

    class Config:
        from_attributes = True