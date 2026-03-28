from http import HTTPStatus
from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm.session import Session
from starlette.status import HTTP_200_OK
from app.schemas.schemas import UserPublicloginScheme, UserloginScheme, CategorySchema, ExpenseSchema
from app.model.datamodel import Category, Expense
from app.database_config import Base, engine, get_db

router = APIRouter(
    prefix="/category",
    tags=["categories"]
)

@router.get("/")
def get_categories(db:Session = Depends(get_db)):
    return db.query(Category).all()

@router.get("/{category_name}", status_code=HTTP_200_OK)
def get_category(category_name: str, db: Session = Depends(get_db)):
    specific_category = db.query(Category).filter(Category.name == category_name).first()

    return specific_category

@router.post("/", status_code=HTTPStatus.CREATED)
def create_category(category: CategorySchema, db:Session = Depends(get_db)):
    new_category = Category(name=category.name, color=category.color, image_url=category.image_url)
    db.add(new_category)
    db.commit()
    return new_category

@router.delete("/")
def delete_category(category_name: str, db:Session = Depends(get_db)):
    category = db.query(Category).filter(Category.name == category_name).first()
    db.delete(category)
    db.commit()
