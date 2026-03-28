from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import joinedload
from schemas.schemas import ExpenseSchema, ExpenseResponseSchema
from model.datamodel import Category, Expense
from database_config.database import Base, engine, get_db
from http import HTTPStatus
from typing import List


router = APIRouter(
    prefix="/expenses",
    tags=["expenses"]
)

@router.get("/", response_model=List[ExpenseResponseSchema])
def get_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).options(joinedload(Expense.categories)).all()

@router.post("/", response_model=ExpenseResponseSchema, status_code=HTTPStatus.CREATED)
def create_expense(expense : ExpenseSchema, db: Session = Depends(get_db)):
    new_expense = Expense(amount=expense.amount, description=expense.description, date=expense.date)

    categories = db.query(Category).filter(Category.id.in_(expense.category_ids)).all()
    if len(categories) != len(expense.category_ids):
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST, detail="One or more category IDs are invalid")

    new_expense.categories.extend(categories)

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

@router.get("/{expense_id}", response_model=ExpenseResponseSchema)
def get_expense(expense_id: int, db: Session = Depends(get_db)):
    expense = db.query(Expense).options(joinedload(Expense.categories)).filter(Expense.id == expense_id).first()
    if expense is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Expense not found")
    return expense
