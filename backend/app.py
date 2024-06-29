from fastapi import FastAPI
from .database import engine, Base
from .models import book, author
from .routes import book_routes, author_routes

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(book_routes.router, prefix="/api/v1")
app.include_router(author_routes.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Bookstore Management System API"}
