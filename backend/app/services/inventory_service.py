from fastapi import HTTPException
from app.models import InventoryMovement

def register_movement(db, *, product, user, quantity, movement_type):
    stock_before = product.stockAvailable

    if movement_type == "entrada":
        product.stockAvailable += quantity
    elif movement_type == "salida":
        if product.stockAvailable < quantity:
            raise HTTPException(400, "Insufficient stock")
        product.stockAvailable -= quantity
    elif movement_type == "ajuste":
        product.stockAvailable = quantity

    stock_after = product.stockAvailable

    movement = InventoryMovement(
        productID=product.id,
        userID=user.id,
        type=movement_type,
        quantity=quantity,
        stockBefore=stock_before,
        stockAfter=stock_after
    )

    db.add(movement)
    db.commit()
    db.refresh(movement)
    return movement
