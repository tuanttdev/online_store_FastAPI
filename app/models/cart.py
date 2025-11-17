from sqlalchemy import Column, String, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class Cart(Base):
    __tablename__ = "carts"
    __table_args__ = {'schema': 'onlinestore'}

    user_id = Column(String, ForeignKey("onlinestore.users.user_id"), primary_key=True)
    product_id = Column(String(20), ForeignKey("onlinestore.products.product_id"), primary_key=True)
    quantity = Column(Numeric)

    product = relationship("Product", back_populates="carts")

