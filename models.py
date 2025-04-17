from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Car(Base): #N
    __tablename__ = "cars"

    id=Column(Integer,primary_key=True,index=True)
    brand=Column(String)
    model=Column(String)
    yearofproduction=Column(Integer)
    category_id=Column(Integer,ForeignKey("categories.id"))
    category=relationship("Category",backref="cars")
class Category(Base): #1
    __tablename__ = "categories"

    id=Column(Integer,primary_key=True,index=True)
    type=Column(String)
