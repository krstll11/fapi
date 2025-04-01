from pydantic import BaseModel, Field, PrivateAttr

class Item(BaseModel):
    name: str=Field(min_length=3)
    price: float 
    description: str
class Find(BaseModel):
    name: str=None
    min_price: float=None
    max_price: float=None
    limit: int=None
