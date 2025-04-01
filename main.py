from typing import Union

from fastapi import FastAPI, Query
from validator import Item

app = FastAPI()
items=[{
    "id":1,
    "name":"laptop",
    "price":1000,
    "description":"This is a laptop"
}]

@app.get("/items/")
def find_items(name:Union[str,None]=None, min_price:Union[float,None]=None,max_price:Union[float,None]=None,limit:Union[int,None]=None):
    yilded_count=1
    for item in items:
        if name and item["name"]!=name:
            continue
        if min_price and item["price"]<min_price:
            continue
        if max_price and item["price"]>max_price:
            continue
        if limit and yilded_count>limit:
            break
        yilded_count+=1
        yield item


@app.get("/items/{item_id}")
def read_item(item_id:int)->Item:
    for item in items:
        if item["id"]==item_id:
            return item


@app.post("/items/")
def create_item(item: Item)->Item:
    item={
    "id":len(items)+1,
    "name":item.name,
    "price":item.price,
    "description":item.description
}
    items.append(item)
    return item