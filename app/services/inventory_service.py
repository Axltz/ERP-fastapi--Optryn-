from fastapi import HTTPException, Depends
from app.models import InventoryMovement
from app.database import get_db

def register_movement(db, *, product, user, quantity, movement_type):
    before = product.stockAvailable 

    if movement_type == "entrada":
        product.stockAvailable += quantity
    elif movement_type == "sell":
        if product.stockAvailable < quantity:
            raise HTTPException(400, "Insufficient Stock")
        product.stockAvailable -= quantity
    elif movement_type == "ajuste":
        if quantity < 0:
            raise HTTPException(400, "Stock cannot be negative value")
        product.stockAvailable = quantity

    after = product.stockAvailable

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
