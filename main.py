from fastapi import FastAPI, HTTPException, Depends
from database import get_db
from sqlalchemy.orm import Session
import models
from typing import List
import pyd

app=FastAPI()

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
async def create_car(car:pyd.CreateProduct,db:Session=Depends(get_db)):
    car_db=models.Car(**car.model_dump())
    db.add(car_db)
    db.commit()
    return car_db
@app.delete("/cars/{car_id}")
async def delete_car(car_id:int,db:Session=Depends(get_db)):
    car=db.query(models.Car).filter(models.Car.id==car_id).first()
    if not car:
        raise HTTPException(status_code=404,detail="Car not found")
    db.delete(car)
    db.commit()
    return car,{"message":"Car deleted"}