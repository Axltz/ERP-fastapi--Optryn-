from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    stockAvaible: int
    stockMinimum: int

class ProductResponse(ProductCreate):
    id: int
    model_config = {
        "from_attributes": True
    }