from fastapi import FastAPI

from app.database_config import Base, engine
from app.routers import categories, expenses, auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(categories.router)
app.include_router(expenses.router)
app.include_router(auth.router)