import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models import Product, InventoryMovement
from datetime import datetime, timezone

# Fixture de la base de datos en memoria
@pytest.fixture(scope="function")
def db_session():
    # Crea un engine en memoria
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    # Crea las tablas
    Base.metadata.create_all(bind=engine)
    
    # Crea la sesión
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)

# Fixture para un producto de prueba
@pytest.fixture
def test_product(db_session):
    product = Product(name="Test Product", price=10.0, stockAvailable=100, stockMinimum=10)
    db_session.add(product)
    db_session.commit()
    db_session.refresh(product)
    return product

# Fixture para un movimiento de inventario de prueba
@pytest.fixture
def test_inventory_movement(db_session, test_product):
    movement = InventoryMovement(
        productID=test_product.id,
        type="entry",
        quantity=20,
        stockBefore=test_product.stockAvailable,
        stockAfter=test_product.stockAvailable + 20,
        date=datetime.now()
    )
    db_session.add(movement)
    db_session.commit()
    db_session.refresh(movement)
    return movement

# Tests
def test_inventory_entry(db_session, test_product):
    initial_stock = test_product.stockAvailable
    quantity_added = 50
    test_product.stockAvailable += quantity_added
    db_session.commit()
    db_session.refresh(test_product)
    assert test_product.stockAvailable == initial_stock + quantity_added

def test_inventory_exit(db_session, test_product):
    initial_stock = test_product.stockAvailable
    quantity_removed = 30
    test_product.stockAvailable -= quantity_removed
    db_session.commit()
    db_session.refresh(test_product)
    assert test_product.stockAvailable == initial_stock - quantity_removed

def test_inventory_adjust(db_session, test_product):
    new_stock = 200
    test_product.stockAvailable = new_stock
    db_session.commit()
    db_session.refresh(test_product)
    assert test_product.stockAvailable == new_stock

def test_get_all_movements(db_session, test_inventory_movement):
    movements = db_session.query(InventoryMovement).all()
    assert len(movements) >= 1
    assert movements[0].productID == test_inventory_movement.productID
