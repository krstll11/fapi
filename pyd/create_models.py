from pydantic import BaseModel,Field
from pyd.base_models import BaseCategory
import models


class CreateProduct(BaseModel):
    brand: str=Field(description="Car brand")
    model: str=Field(description="Car model")
    yearofproduction: int=Field(gt=1900,lt=2025,description="year of production must be between 1900 and 2024")
    category_id: int
    mileage: int
class CreateCategory(BaseModel):
    type: str
class CreateUser(BaseModel):
    username: str
    password: str
