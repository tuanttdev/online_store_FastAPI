from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"
    __table_args__ = {'schema': 'onlinestore'}

    product_id = Column(String(20), primary_key=True)
    name = Column(String(500))
    type = Column(String)
    uom_id = Column(String(20))
    price = Column(Float)
    decription = Column(String(5000))

    carts = relationship("Cart", back_populates="product")