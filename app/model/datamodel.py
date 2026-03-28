from sqlalchemy import Column, Integer, String, DateTime, Double, ForeignKey, Table, func
from sqlalchemy.orm import relationship
from database_config.database import Base

expense_category_association_table = Table(
    'expense_category_association', Base.metadata,
    Column('expense_id', Integer, ForeignKey('Expense.id')),
    Column('category_id', Integer, ForeignKey('Category.id'))
)

class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    image_url = Column(String(50))
    color = Column(String(10))
    expenses = relationship("Expense", secondary=expense_category_association_table, back_populates="categories")

class Expense(Base):
    __tablename__ = 'Expense'
    id = Column(Integer, primary_key=True)
    amount = Column(Double, nullable=False)
    description = Column(String(50), nullable=True)
    date = Column(DateTime, nullable=False)
    categories = relationship("Category", secondary=expense_category_association_table, back_populates="expenses")

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(30), nullable=False)
    created_at = Column(DateTime, default=func.now())
