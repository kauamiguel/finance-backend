from http import HTTPStatus
from fastapi import FastAPI, Depends
from sqlalchemy.orm.session import Session
from schemas.schemas import UserPublicloginScheme, UserloginScheme, CategorySchema, ExpenseSchema
from model.datamodel import Category, Expense
from database_config import Base, engine, get_db
from routers import categories

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(categories.router)
