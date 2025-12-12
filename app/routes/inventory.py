from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Product, InventoryMovement
from app.services.auth_service import get_current_user
from app.services.inventory_service import register_movement

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.post("/entrada")
def inventory_entry(productID: int, quantity: int,
                    db: Session = Depends(get_db),
                    current_user= Depends(get_current_user)):
    
    product = db.query(Product).filter(product.id == productID).first()
    if not product:
        raise HTTPException(404, "product no found")
    
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
            "product_id": movement.product_id,
            "type": movement.type,
            "quantity": movement.quantity,
            "stock_before": movement.stock_before,
            "stock_after": movement.stock_after,
            "date": movement.date
        }

    }
@router.post("/ajuste")
def inventory_adjust(product_id: int, new_stock: int,
                     db: Session = Depends(get_db),
                     current_user=Depends(get_current_user)):

    product = db.query(Product).filter(Product.id == product_id).first()
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
            "product_id": movement.product_id,
            "type": movement.type,
            "quantity": movement.quantity,
            "stock_before": movement.stock_before,
            "stock_after": movement.stock_after,
            "date": movement.date
        }
    }

@router.get("/movimientos/{product_id}")
def get_movements(product_id: int,
                  db: Session = Depends(get_db),
                  current_user=Depends(get_current_user)):

    movements = db.query(InventoryMovement).filter(
        InventoryMovement.product_id == product_id
    ).order_by(InventoryMovement.date.desc()).all()

    return movements
