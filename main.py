from http import HTTPStatus
from fastapi import FastAPI, Depends
from sqlalchemy.orm.session import Session
from schemas.schemas import Category, UserPublicloginScheme, UserloginScheme
from database_config import Base, engine, get_db

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def get_categories():
    return ""

@app.post("/category", status_code=HTTPStatus.CREATED, response_model=Category)
def create_category(category: Category, db:Session = Depends(get_db)):
    return ...

@app.post("/login", status_code=HTTPStatus.CREATED, response_model=UserPublicloginScheme)
def user_login(user: UserloginScheme):
    return user
