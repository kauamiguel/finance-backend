from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, EmailStr

class UserloginScheme(BaseModel):
    username : str
    email: EmailStr
    password: str

class UserPublicloginScheme(BaseModel):
    username : str
    email: EmailStr

class CategoryBase(BaseModel):
    id: int
    name : str
    image_url : str
    color : str

    class Config:
        orm_mode = True

class CategorySchema(BaseModel):
    name : str
    image_url : str
    color : str

class ExpenseBase(BaseModel):
    amount : float
    description : str
    date : datetime

class ExpenseSchema(ExpenseBase):
    category_ids : List[int]

class ExpenseResponseSchema(ExpenseBase):
    id: int
    categories: List[CategoryBase] = []

    class Config:
        orm_mode = True
