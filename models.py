from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import datetime

class Car(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String)
    yearofproduction = Column(Integer)
    mileage = Column(Integer)
    image = Column(String,default="")
    dateinsystem = Column(String, default=datetime.datetime.now)
    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", backref="cars")  
    

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
class User(Base):
    __tablename__="users"
    id= Column(Integer, primary_key=True, index=True)
    username= Column(String)
    password= Column(String)


