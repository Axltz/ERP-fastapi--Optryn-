import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database import Base, get_db
from app.models import User, Product

# ---- DB TEST ----
SQLALCHEMY_DATABASE_URL = "sqlite:///./basetest.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

# ---- FIXTURE DB ----
@pytest.fixture(scope="function")
def db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

# ---- OVERRIDE DB ----
@pytest.fixture(scope="function")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

# ---- USERS ----
@pytest.fixture
def admin_user(db):
    user = User(username="admin", hashed_password="hashed", role="admin")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@pytest.fixture
def normal_user(db):
    user = User(username="user", hashed_password="hashed", role="user")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# ---- PRODUCT ----
@pytest.fixture
def sample_product(db):
    product = Product(
        name="Test Product",
        price=100,
        stockAvailable=10
    )
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
