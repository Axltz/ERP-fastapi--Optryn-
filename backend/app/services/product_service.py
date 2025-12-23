from sqlalchemy.orm import Session
from app.models import Product
from app.schemas.product import ProductCreate

def create_product(db: Session, data: ProductCreate) -> Product:
    product = Product(name=data.name, price=data.price, stockAvailable=data.stockAvailable, stockMinimum=data.stockMinimum)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return (
        db.query(Product)
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product_db(db: Session, product: Product, data: ProductCreate):
    product.name = data.name
    product.price = data.price
    product.stockMinimun = data.stockMinimum
    product.stockAvailable = data.stockAvailable
    db.commit()
    db.refresh(product)
    return product

def delete_product_db(db: Session, product: Product):
    db.delete(product)
    db.commit()
