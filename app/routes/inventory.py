from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import datetime
from app.database import get_db
from app.models import Product, InventoryMovement
from app.services.auth_service import get_current_user
from app.services.inventory_service import register_movement

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.post("/entrada")
def inventory_entry(productID: int, quantity: int,
                    db: Session = Depends(get_db),
                    current_user=Depends(get_current_user)):

    product = db.query(Product).filter(Product.id == productID).first()
    if not product:
        raise HTTPException(404, "Product not found")

    movement = register_movement(
        db,
        product=product,
        user=current_user,
        quantity=quantity,
        movement_type="entrada"
    )

    return {
        "message": "Stock increased successfully",
        "movement": {
            "id": movement.id,
            "product_id": movement.productID,
            "type": movement.type,
            "quantity": movement.quantity,
            "stock_before": movement.stockBefore,
            "stock_after": movement.stockAfter,
            "date": movement.date
        }
    }


@router.post("/salida")
def inventory_exit(productID: int, quantity: int,
                   db: Session = Depends(get_db),
                   current_user=Depends(get_current_user)):

    product = db.query(Product).filter(Product.id == productID).first()
    if not product:
        raise HTTPException(404, "Product not found")

    movement = register_movement(
        db,
        product=product,
        user=current_user,
        quantity=quantity,
        movement_type="salida"
    )

    return {
        "message": "Stock decreased successfully",
        "movement": {
            "id": movement.id,
            "product_id": movement.productID,
            "type": movement.type,
            "quantity": movement.quantity,
            "stock_before": movement.stockBefore,
            "stock_after": movement.stockAfter,
            "date": movement.date
        }
    }


@router.post("/ajuste")
def inventory_adjust(productID: int, new_stock: int,
                     db: Session = Depends(get_db),
                     current_user=Depends(get_current_user)):

    product = db.query(Product).filter(Product.id == productID).first()
    if not product:
        raise HTTPException(404, "Product not found")

    movement = register_movement(
        db,
        product=product,
        user=current_user,
        quantity=new_stock,
        movement_type="ajuste"
    )

    return {
        "message": "Stock adjusted successfully",
        "movement": {
            "id": movement.id,
            "product_id": movement.productID,
            "type": movement.type,
            "quantity": movement.quantity,
            "stock_before": movement.stockBefore,
            "stock_after": movement.stockAfter,
            "date": movement.date
        }
    }


@router.get("/movimientos")
def get_all_movements(
    movement_type: str | None = Query(None, description="Filter by type: entrada, salida, ajuste"),
    start_date: datetime | None = Query(None, description="Start date in ISO format"),
    end_date: datetime | None = Query(None, description="End date in ISO format"),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    query = db.query(InventoryMovement)

    if movement_type:
        query = query.filter(InventoryMovement.type == movement_type)
    if start_date:
        query = query.filter(InventoryMovement.date >= start_date)
    if end_date:
        query = query.filter(InventoryMovement.date <= end_date)

    movements = query.order_by(InventoryMovement.date.desc()).all()
    return movements
