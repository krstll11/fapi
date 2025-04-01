from typing import Union

from fastapi import FastAPI, Query
import random
import math

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
@app.get("/about_me")
def display_about_me():
    return {"name": "I am a student",
            "group": "ISIT-323901"
            }
@app.get("/random_number")
def display_random_number():
    return {"random_number": random.randint(1, 100)}
@app.post("/triangle")
def s_display_triangle(a: int=Query(gt=0), b: int=Query(gt=0), c: int=Query(gt=0)):
        if a+b<=c or a+c<=b or b+c<=a:
            return {"error": "no triangle"}
        else:
            p=(a+b+c)/2
            return {math.sqrt(p*(p-a)*(p-b)*(p-c))}