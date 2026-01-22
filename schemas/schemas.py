from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserloginScheme(BaseModel):
    username : str
    email: EmailStr
    password: str

class UserPublicloginScheme(BaseModel):
    username : str
    email: EmailStr

class Category(BaseModel):
    name : str
    image_url : str
    color : str

class Expense(BaseModel):
    amount : float
    description : str
    date : datetime
    category : Category
