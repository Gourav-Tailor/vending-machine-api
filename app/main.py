# app/main.py

from fastapi import FastAPI, Header, HTTPException
from typing import List, Optional

app = FastAPI(title="Vending Machine API", version="1.0.0")
