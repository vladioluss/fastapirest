from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    price: float
    

items = [
    {'id': 1, 'name': 'nnnnn', 'price': 3.3},
    {'id': 2, 'name': 'nametest', 'price': 6.4}
]

@app.get("/items", response_model=List[Item])
async def read_items():
    return items

@app.post("/items", response_model=Item)
async def create_item(item: Item):
    items.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    items[item_id] = item
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    del items[item_id]
    return {"message": "Item deleted"}
    
    
