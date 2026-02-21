# app/schemas.py

from pydantic import BaseModel
from typing import List


class Item(BaseModel):
    id: str
    name: str
    price_cents: int
    quantity: int

