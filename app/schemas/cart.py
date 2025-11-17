from pydantic import BaseModel
from typing import Optional

class CartItemOut(BaseModel):
    product_id: str
    product_name: str
    product_type: str
    quantity: int
    uom_id: str
    price: float
    image_url: str

    class Config:
        orm_mode = True

class CartCreate(BaseModel):
    user_id: str
    product_id: str
    quantity: int
