from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.product import Product
from app.schemas.product import ProductOut, ProductPage
from typing import List
import random


router = APIRouter()

@router.get("/products", response_model=ProductPage)
def get_all_products(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Page size"),
    db: Session = Depends(get_db)

):

    skip = (page - 1) * page_size
    total = db.query(Product).count()
    raw_products = db.query(Product).offset(skip).limit(page_size).all()

    products = [
        ProductOut(
            product_id=p.product_id,
            name=p.name,
            type=p.type,
            uom_id=p.uom_id,
            decription=p.decription,
            price=round(random.uniform(100000, 500000)),
            image_url="https://via.placeholder.com/150"
        )
        for p in raw_products
    ]

    return ProductPage(
        total=total,
        page=page,
        page_size=page_size,
        items=products
    )

@router.get("/products/{product_id}", response_model=ProductOut)
def get_product(product_id: str, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return ProductOut(
        product_id=product.product_id,
        name=product.name,
        type=product.type,
        uom_id=product.uom_id,
        decription=product.decription,
        price=round(random.uniform(100000, 500000)),  # tạo giá tạm
        image_url="https://via.placeholder.com/300"  # hình tạm
    )