from pydantic import BaseModel
from .book import Book  # Ensures Book is imported

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    books: list[Book] = []  # Use the imported Book schema

    class Config:
        orm_mode = True
