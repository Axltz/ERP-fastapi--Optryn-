from sqlalchemy.orm import Session
from app.models import Product
from app.schemas.product import ProductCreate

def create_product(db: Session, data: ProductCreate) -> Product:
    product = Product(name=data.name, price=data.price, stock=data.stock)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def get_products(db: Session):
    return db.query(Product).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product_db(db: Session, product: Product, data: ProductCreate):
    product.name = data.name
    product.price = data.price
    product.stock = data.stock
    db.commit()
    db.refresh(product)
    return product

def delete_product_db(db: Session, product: Product):
    db.delete(product)
    db.commit()
