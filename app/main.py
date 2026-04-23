from http import HTTPStatus

from fastapi import Depends, FastAPI
from sqlalchemy.orm.session import Session

from app.database_config import Base, engine, get_db
from app.model.datamodel import Category, Expense
from app.routers import categories, expenses
from app.schemas.schemas import (
    CategorySchema,
    ExpenseSchema,
    UserloginScheme,
    UserPublicloginScheme,
)

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(categories.router)
app.include_router(expenses.router)
