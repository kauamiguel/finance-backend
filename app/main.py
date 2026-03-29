from http import HTTPStatus
from fastapi import FastAPI, Depends
from sqlalchemy.orm.session import Session
from app.schemas.schemas import UserPublicloginScheme, UserloginScheme, CategorySchema, ExpenseSchema
from app.model.datamodel import Category, Expense
from app.database_config import Base, engine, get_db
from app.routers import categories, expenses

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(categories.router)
app.include_router(expenses.router)