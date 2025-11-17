from fastapi import FastAPI
from .api.v1 import user , product, cart
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user.router, prefix="/api/v1/user", tags=["User"])
app.include_router(product.router, prefix="/api/v1/product", tags=["Product"])
app.include_router(cart.router, prefix="/api/v1/cart", tags=["Cart"])