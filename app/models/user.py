from sqlalchemy import Column, String, DateTime
from app.db.base import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'schema': 'onlinestore'}

    user_id = Column(String(20), primary_key=True, index=True)
    account_name = Column(String(50), unique=True, nullable=False)
    password = Column(String(512), nullable=False)
    user_type = Column(String(20))
    email = Column(String(256), unique=True)
    phone_number = Column(String(20))
    address = Column(String(256))
    registation_date = Column(DateTime, default=datetime.utcnow)