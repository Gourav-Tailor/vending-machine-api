# app/schemas.py

from pydantic import BaseModel
from typing import List


class Item(BaseModel):
    id: str
    name: str
    price_cents: int
    quantity: int


class ErrorResponse(BaseModel):
    error_code: str
    message: str


class VendRequest(BaseModel):
    item_id: str
    payment_cents: int


class VendSuccessResponse(BaseModel):
    vended_item_id: str
    change_returned_cents: int