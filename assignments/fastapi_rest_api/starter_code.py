"""Starter FastAPI application for the Simple Items Service assignment.

Run with:
    uvicorn assignments.fastapi_rest_api.starter_code:app --reload --port 8000

"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Simple Items Service")


class Item(BaseModel):
    name: str
    description: str | None = None


# In-memory store: id -> Item
_store: Dict[int, Item] = {}
_next_id = 1


@app.get("/items")
def list_items():
    return [{"id": i, **_store[i].dict()} for i in sorted(_store.keys())]


@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in _store:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": item_id, **_store[item_id].dict()}


@app.post("/items", status_code=201)
def create_item(item: Item):
    global _next_id
    item_id = _next_id
    _store[item_id] = item
    _next_id += 1
    return {"id": item_id, **item.dict()}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in _store:
        raise HTTPException(status_code=404, detail="Item not found")
    _store[item_id] = item
    return {"id": item_id, **item.dict()}


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in _store:
        raise HTTPException(status_code=404, detail="Item not found")
    del _store[item_id]
