from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime
from pydantic import BaseModel
from app.database import get_db
from app.models import Product, InventoryMovement
from app.services.auth_service import get_current_user
from app.services.inventory_service import register_movement

router = APIRouter(prefix="/inventory", tags=["Inventory"])

class InventoryEntry(BaseModel):
    productID: int
    quantity: int

class InventoryExit(BaseModel):
    productID: int
    quantity: int

class InventoryAdjust(BaseModel):
    productID: int
    new_stock: int

