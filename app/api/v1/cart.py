from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.cart import Cart
from app.models.user import User
from app.models.product import Product
from app.schemas.cart import CartItemOut, CartCreate
from typing import List
import random

router = APIRouter()

@router.get("/cart/{user_id}", response_model=list[CartItemOut])
def get_product(user_id: str, db: Session = Depends(get_db)):
    carts = db.query(Cart).filter(Cart.user_id == user_id).all()

    if not carts:
        raise HTTPException(status_code=404, detail="There is no product on your cart")

    result = []

    for cart in carts:
        if cart.product is None:
            carts.remove(cart)

        item = {
            "product_id": cart.product_id,
            "product_name": cart.product.name,
            "uom_id": cart.product.uom_id,
            "price": cart.product.price,
            "quantity": cart.quantity,
            "product_type" : cart.product.type,
            "image_url" : "https://via.placeholder.com/150",
        }
        result.append(item)

    return result

@router.post("/cart/add")
def add_to_cart(cart_data: CartCreate, db: Session = Depends(get_db)):
    # Kiểm tra user tồn tại
    user = db.query(User).filter(User.user_id == cart_data.user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User does not exist")

    # Kiểm tra product tồn tại
    product = db.query(Product).filter(Product.product_id == cart_data.product_id).first()
    if not product:
        raise HTTPException(status_code=400, detail="Product does not exist")

    existing = db.query(Cart).filter(
        Cart.user_id == cart_data.user_id,
        Cart.product_id == cart_data.product_id
    ).first()

    if existing:
        existing.quantity += cart_data.quantity
    else:
        new_cart = Cart(**cart_data.dict())
        db.add(new_cart)

    db.commit()
    return {"message": "Added to cart successfully"}

@router.post("/cart/deleteItem")
def delete_item_from_cart(cart_data: CartCreate, db: Session = Depends(get_db)):
    # Kiểm tra user tồn tại
    user = db.query(User).filter(User.user_id == cart_data.user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User does not exist")

    # Kiểm tra product tồn tại
    product = db.query(Product).filter(Product.product_id == cart_data.product_id).first()
    if not product:
        raise HTTPException(status_code=400, detail="Product does not exist")

    existing = db.query(Cart).filter(
        Cart.user_id == cart_data.user_id,
        Cart.product_id == cart_data.product_id
    ).first()
    if not existing :
        raise HTTPException(status_code=400, detail="Item does not exist in your cart")
    else:
        db.delete(existing)

    db.commit()
    return {"message": "Added to cart successfully"}