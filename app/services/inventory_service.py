from fastapi import HTTPException, Depends
from app.models import InventoryMovement
from app.database import get_db

def register_movement(db, *, product, user, quantity, movement_type):
    before = product.stock_actual

    if movement_type == "entrada":
        product.stock_actual += quantity
    elif movement_type == "salida":
        if product.stock_actual < quantity:
            raise HTTPException(400, "Stock insuficiente")
        product.stock_actual -= quantity
    elif movement_type == "ajuste":
        product.stock_actual = quantity 
    after = product.stock_actual

    movement = InventoryMovement(
        product_id=product.id,
        user_id=user.id,
        type=movement_type,
        quantity=quantity,
        stock_before=before,
        stock_after=after
    )

    db.add(movement)
    db.commit()
    db.refresh(movement)
    return movement
