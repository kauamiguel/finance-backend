from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Double, ForeignKey
from database_config.database import Base

class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    image_url = Column(String(50))
    color = Column(String(10))

class Expense(Base):
    __tablename__ = 'Expense'
    id = Column(Integer, primary_key=True)
    amount = Column(Double, nullable=False)
    description = Column(String(50), nullable=True)
    date = Column(DateTime, nullable=False)
    category_id = Column(Integer, ForeignKey('Category.id'))

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(30), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
