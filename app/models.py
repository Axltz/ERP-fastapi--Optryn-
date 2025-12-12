import datetime 
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False, default="user")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stockAvaible = Column(Integer, nullable=False, default=0)
    stockMinimun = Column(Integer, nullable=False, default=0)

class InventoryMovement(Base):
    __tablename__ = "inventory_movements"

    id = Column(Integer, primary_key=True, index=True)
    productID = Column(Integer, ForeignKey("products.id"), nullable=False)
    type = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    stockBefore = Column(Integer, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)

    userID = Column(Integer, ForeignKey("users.id"))

    product = relationship("Product")
    user = relationship("User")

    