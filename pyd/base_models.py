from pydantic import BaseModel, Field

class BaseProduct(BaseModel):
    id: int=Field(example="1")
    brand: str=Field(example="BMW")
    model: str=Field(example="X5")
    yearofproduction: int=Field(example="2020")
    category_id: int=Field(example="1")
    mileage: int=Field(example="10000")
    dateinsystem: str=Field(example="2022-01-01")
    image: str=Field("",example="https://example.com/image.jpg")

class BaseCategory(BaseModel):
    id: int
    type: str
class User(BaseModel):
    id: int
    username: str
    password: str



