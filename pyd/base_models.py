from pydantic import BaseModel, Field

class BaseProduct(BaseModel):
    id: int=Field(example="1")
    brand: str=Field(example="BMW")
    model: str=Field(example="X5")
    yearofproduction: int=Field(example="2020")
class BaseCategory(BaseModel):
    id: int
    type: str
