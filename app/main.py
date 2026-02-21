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

