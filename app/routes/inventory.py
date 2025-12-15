from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from app.models import Product, InventoryMovement, User
from app.services.auth_service import require_role
from app.services.inventory_service import register_movement
from app.schemas.inventory import (
    InventoryEntry,
    InventoryExit,
    InventoryAdjust,
)

router = APIRouter(tags=["Inventory"])


@router.post("/entrada")
def inventory_entry(
    data: InventoryEntry,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("admin")),
):
    product = db.query(Product).filter(Product.id == data.productID).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    movement = register_movement(
        db=db,
        product=product,
        user=current_user,
        quantity=data.quantity,
        movement_type="entrada",
    )

    return {"message": "Stock increased successfully"}


@router.post("/salida")
def inventory_exit(
    data: InventoryExit,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("admin")),
):
    product = db.query(Product).filter(Product.id == data.productID).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    movement = register_movement(
        db=db,
        product=product,
        user=current_user,
        quantity=data.quantity,
        movement_type="salida",
    )

    return {"message": "Stock decreased successfully"}


@router.post("/ajuste")
def inventory_adjust(
    data: InventoryAdjust,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("admin")),
):
    product = db.query(Product).filter(Product.id == data.productID).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    movement = register_movement(
        db=db,
        product=product,
        user=current_user,
        quantity=data.new_stock,
        movement_type="ajuste",
    )

    return {"message": "Stock adjusted successfully"}


@router.get("/movimientos")
def get_all_movements(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_role("admin")),
):
    return db.query(InventoryMovement).all()
