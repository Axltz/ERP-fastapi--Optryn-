from fastapi import HTTPException, Depends
from app.models import InventoryMovement
from app.database import get_db

def register_movement(db, *, product, user, quantity, movement_type):
    before = product.stockAvaible

    if movement_type == "entrada":
        product.stockAvaible += quantity
    elif movement_type == "salida":
        if product.stockAvaible < quantity:
            raise HTTPException(400, "Stock insuficiente")
        product.stockAvaible -= quantity
    elif movement_type == "ajuste":
        product.stockAvaible = quantity 
    after = product.stockAvaible

    movement = InventoryMovement(
        productID=product.id,
        userID=user.id,
        type=movement_type,
        quantity=quantity,
        stockBefore=before,
        stockAfter=after
                )

    db.add(movement)
    db.commit()
    db.refresh(movement)
    return movement
