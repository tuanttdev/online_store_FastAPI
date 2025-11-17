from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password
from app.core.auth import decode_access_token
from app.db.session import get_db
from fastapi import HTTPException, status, Depends


def create_user(db: Session, user_data: UserCreate):
    existing_user = db.query(User).filter(User.account_name == user_data.account_name).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Account name already exists")

    hashed_pwd = hash_password(user_data.password)
    user = User(**user_data.dict())
    user.password = hashed_pwd

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, account_name: str, password: str):
    user = db.query(User).filter(User.account_name == account_name).first()
    if not user or not verify_password(password, user.password):
        return None
    return user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    username = decode_access_token(token)
    if username is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.account_name == username).first()
    return user