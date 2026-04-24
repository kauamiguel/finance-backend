from http import HTTPStatus
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.schemas import (
    UserloginScheme,
    UserRegisterScheme,
)
from app.database_config import get_db
from app.model.datamodel import User

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login_user(user: UserloginScheme, db: Session = Depends(get_db)):
    existent_user = db.query(User).filter(User.email == user.email).first()
    if not existent_user:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail="Invalid user"
        )
    if existent_user.password != user.password:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED, detail="Invalid password"
        )
    return f"User autenticated: {existent_user.email}"

@router.post("/register")
def register_user(user: UserRegisterScheme, db: Session = Depends(get_db)):
    existent_user = db.query(User).filter(User.email == user.email).first()
    if existent_user:
        raise HTTPException(
            status_code=HTTPStatus.CONFLICT,
            detail="User already registered"
        )
    new_user = User(email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return f"User registered: {new_user.email}"
