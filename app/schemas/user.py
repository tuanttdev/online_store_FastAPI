from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    user_id: str
    account_name: str
    password: str
    email: EmailStr
    phone_number: Optional[str] = None
    address: Optional[str] = None
    user_type: Optional[str] = "customer"

class UserLogin(BaseModel):
    account_name: str
    password: str

class UserOut(BaseModel):
    user_id: str
    account_name: str
    email: EmailStr
    user_type: str
    registation_date: datetime

    class Config:
        orm_mode = True