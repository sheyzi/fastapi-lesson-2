from fastapi import FastAPI, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class ItemModel(BaseModel):
    name: str
    description: str
    price: float

inventory = {
    1: {
        "name": "Peak Milk",
        "description": "Sweet beautiful milk",
        "price": 250.00
    },
    2: {
        "name": "Nasco Cornflakes",
        "description": "Sweet beautiful cornflakes",
        "price": 100.00
    },
    3: {
        "name": "Golden Morn",
        "description": "Sweet beautiful gorden morn",
        "price": 120.00
    },
}

@app.get('/')
def get_all_items(min_price: Optional[float] = None):
    if min_price:
        items = []
        for key, value in inventory.items():
            if value['price'] >= min_price:
                items.append(inventory[key])
        return items
    return inventory

@app.get("/{item_id}")
def get_item_with_id(item_id: int):
    if inventory.get(item_id) is None:
        raise HTTPException(404, detail=f"Item with id {item_id} doesn't exist!")
    return inventory[item_id]

@app.post('/{item_id}', status_code=status.HTTP_201_CREATED)
def add_new_item_to_inventory(item_id: int, item: ItemModel):
    if inventory.get(item_id) is not None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=f"Item with id {item_id} exists!")
    inventory[item_id] = item.dict()
    return item

@app.put('/{item_id}')
def update_item(item_id: int, item: ItemModel):
    if inventory.get(item_id) is None:
        raise HTTPException(404, detail=f"Item with id {item_id} doesn't exist!")
    inventory[item_id] = item.dict()
    return inventory[item_id]

@app.delete("/{item_id}")
def delete_item(item_id: int):
    if inventory.get(item_id) is None:
        raise HTTPException(404, detail=f"Item with id {item_id} doesn't exist!")
    del inventory[item_id]
    return {"msg": "Item deleted!"}