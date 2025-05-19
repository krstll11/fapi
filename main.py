from fastapi import FastAPI, HTTPException, Depends, UploadFile, status
from database import get_db
from sqlalchemy.orm import Session
import models
from typing import List
import pyd
import uuid
from PIL import Image
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Response
from typing import Annotated
from passlib.context import CryptContext

app=FastAPI()
security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
@app.post("/register")
def register(user: pyd.CreateUser, db: Session = Depends(get_db)):
    
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    
    hashed_password = pwd_context.hash(user.password)
    new_user = models.User(username=user.username, password=hashed_password)
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}
def authenticate_user(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == credentials.username).first()
    if not user or not pwd_context.verify(credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return user
@app.get("/authenticate test")
def protected_route(current_user: models.User = Depends(authenticate_user)):
    return {"message": "Authenticated successfully", "username": current_user.username}
@app.get("/cars",response_model=List[pyd.SchemaCar])
async def get_cars(db:Session=Depends(get_db)):
    cars=db.query(models.Car).all()
    
    return cars
@app.get("/cars/{car_id}",response_model=pyd.SchemaCar)
async def get_car(car_id:int,db:Session=Depends(get_db)):
    car=db.query(models.Car).filter(models.Car.id==car_id).first()
    if not car:
        raise HTTPException(status_code=404,detail="Car not found")
    return car
@app.post("/cars",response_model=pyd.BaseProduct)
async def create_car(car:pyd.CreateProduct,db:Session=Depends(get_db),current_user: models.User = Depends(authenticate_user)):
    car_db=models.Car(**car.model_dump())
    db.add(car_db)
    db.commit()
    return car_db
@app.delete("/cars/{car_id}")
async def delete_car(car_id:int,db:Session=Depends(get_db),current_user: models.User = Depends(authenticate_user)):
    car=db.query(models.Car).filter(models.Car.id==car_id).first()
    if not car:
        raise HTTPException(status_code=404,detail="Car not found")
    db.delete(car)
    db.commit()
    return car,{"message":"Car deleted"}
@app.put("/cars/{car_id}",response_model=pyd.BaseProduct)
async def update_car(car_id:int,car:pyd.CreateProduct,db:Session=Depends(get_db),current_user: models.User = Depends(authenticate_user)):
    car_db=db.query(models.Car).filter(models.Car.id==car_id).first()
    if not car_db:
        raise HTTPException(status_code=404,detail="Car not found")
    car_db.brand=car.brand
    car_db.model=car.model
    car_db.yearofproduction=car.yearofproduction
    car_db.mileage=car.mileage
    db.commit()
    return car_db
@app.post("/categories",response_model=pyd.BaseCategory)
async def create_category(category:pyd.CreateCategory,db:Session=Depends(get_db),current_user: models.User = Depends(authenticate_user)):
    category_db=models.Category(**category.model_dump())
    db.add(category_db)
    db.commit()
    return category_db
@app.get("/categories",response_model=List[pyd.CreateCategory])
async def get_categories(db:Session=Depends(get_db)):
    categories=db.query(models.Category).all()
    
    return categories
@app.put("/carimage/{car_id}",response_model=pyd.BaseProduct)
async def create_upload_file(file: UploadFile,car_id:int,db:Session=Depends(get_db),current_user: models.User = Depends(authenticate_user)):
    car_db=db.query(models.Car).filter(models.Car.id==car_id).first()
    if not car_db:
        raise HTTPException(status_code=404,detail="Car not found")
    file.file.read()
    size_mb=file.file.tell()/1024/1024
    file.file.seek(0)
    if size_mb>2:
        raise HTTPException(status_code=400,detail="File size must be less than 2MB")
    file_extension = file.filename.split(".")[-1] if "." in file.filename else ""
    if file_extension not in ["jpg", "jpeg", "png"]:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    unique_filename = f"{uuid.uuid4()}.{file_extension}" if file_extension else f"{uuid.uuid4()}"
    file_location = f"images/{unique_filename}"
    
    with open(file_location, "wb") as file_object:
        file_object.write(file.file.read())
    car_db.image = file_location
    db.commit()
    return car_db
