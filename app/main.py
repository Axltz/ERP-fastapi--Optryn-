from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, products, inventory



app = FastAPI(title="Optryn API")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(inventory.router, prefix="/inventory", tags=["Inventory"])
