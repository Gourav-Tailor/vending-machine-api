# app/store.py

from typing import Dict

INVENTORY: Dict[str, dict] = {
    "A1": {"id": "A1", "name": "Cola", "price_cents": 150, "quantity": 5},
    "B1": {"id": "B1", "name": "Chips", "price_cents": 100, "quantity": 3},
    "C1": {"id": "C1", "name": "Water", "price_cents": 75, "quantity": 10},
}