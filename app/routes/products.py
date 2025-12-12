from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, ProductResponse
from app.models import Product, User
from app.database import get_db
from app.services.auth_service import get_current_user, require_role
from app.services.product_service import create_product, get_products, get_product_by_id, update_product_db, delete_product_db

router = APIRouter()

@router.post("/", response_model=ProductResponse)
def create_product_route(data: ProductCreate,
                         db: Session = Depends(get_db),
                         current_user: User = Depends(require_role("admin"))):
    return create_product(db, data)

@router.get("/", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    return get_products(db)

@router.get("/{product_id}", response_model=ProductResponse)
def get_product_route(product_id: int,
                      db: Session = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=ProductResponse)
def update_product_route(product_id: int, data: ProductCreate,
                         db: Session = Depends(get_db),
                         current_user: User = Depends(require_role("admin"))):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return update_product_db(db, product, data)

@router.delete("/{product_id}")
def delete_product_route(product_id: int,
                         db: Session = Depends(get_db),
                         current_user: User = Depends(require_role("admin"))):
    product = get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    delete_product_db(db, product)
    return {"message": "Product deleted successfully"}
