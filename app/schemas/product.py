from pydantic import BaseModel
from typing import Optional

class ProductOut(BaseModel):
    product_id: str
    name: Optional[str]
    type: Optional[str]
    uom_id: Optional[str]
    decription: Optional[str]
    price: float
    image_url: str

    class Config:
        orm_mode = True

class ProductPage(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[ProductOut]

