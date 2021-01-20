#!/usr/bin/env python3
from typing import Optional, Dict

import uvicorn
from fastapi import FastAPI
from mangum import Mangum
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="FastAPI Mangum Example", version='1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class DiffEntityBody(BaseModel):
    old:dict
    new:dict

handler = Mangum(app)


@app.get('/', name='Hello World', tags=['Hello'])
def hello_world():
    return {"Hello": "Python"}

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.post("/diff/")
async def diff_items(diff:DiffEntityBody):
    return diff

if __name__ == '__main__':
    uvicorn.run(app)

