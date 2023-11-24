import uvicorn

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[str, None] = None

@app.get("/")
def read_root():
    return {"Hello":"World"}


@app.get("/items/{id}")
def read_item(id:int, q: Union[str, None] = None):
    return {"id":id,"q":q}

@app.put("/item/{id}")
def update_item(id: int, item: Item):
    return {"id":id,"item":item}



def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("proj2.main:app", host="0.0.0.0", port=8000, reload=True)