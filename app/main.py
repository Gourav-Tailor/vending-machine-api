# app/main.py

from fastapi import FastAPI, Header, HTTPException
from typing import List, Optional
from app.schemas import *
from app.store import INVENTORY

app = FastAPI(title="Vending Machine API", version="1.0.0")


def validate_machine_id(machine_id: Optional[str]):
    if not machine_id:
        raise HTTPException(
            status_code=400,
            detail={
                "error_code": "MISSING_MACHINE_ID",
                "message": "X-Machine-Id header is required.",
            },
        )


@app.get("/inventory", response_model=List[Item])
def get_inventory(x_machine_id: Optional[str] = Header(None)):
    validate_machine_id(x_machine_id)
    return list(INVENTORY.values())


@app.post("/vend", response_model=VendSuccessResponse)
def vend_item(
    request: VendRequest,
    x_machine_id: Optional[str] = Header(None),
):
    validate_machine_id(x_machine_id)

    item = INVENTORY.get(request.item_id)

    if not item:
        raise HTTPException(
            status_code=404,
            detail={
                "error_code": "ITEM_NOT_FOUND",
                "message": "Item does not exist.",
            },
        )

    if item["quantity"] <= 0:
        raise HTTPException(
            status_code=404,
            detail={
                "error_code": "OUT_OF_STOCK",
                "message": "Item is out of stock.",
            },
        )

    if request.payment_cents < item["price_cents"]:
        # Special A1 hardware quirk
        if request.item_id == "A1":
            error_code = "A1_BROKE"
        else:
            error_code = "INSUFFICIENT_FUNDS"

        raise HTTPException(
            status_code=400,
            detail={
                "error_code": error_code,
                "message": "Payment amount is less than the item price.",
            },
        )

    item["quantity"] -= 1
    change = request.payment_cents - item["price_cents"]

    return {
        "vended_item_id": request.item_id,
        "change_returned_cents": change,
    }