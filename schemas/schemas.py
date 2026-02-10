from datetime import datetime
from pydantic import BaseModel, EmailStr

class UserloginScheme(BaseModel):
    username : str
    email: EmailStr
    password: str

class UserPublicloginScheme(BaseModel):
    username : str
    email: EmailStr

class CategorySchema(BaseModel):
    name : str
    image_url : str
    color : str

class ExpenseSchema(BaseModel):
    amount : float
    description : str
    date : datetime
    category : CategorySchema
