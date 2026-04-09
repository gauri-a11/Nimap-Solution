from fastapi import FastAPI
from app.database.init_db import init_db
from app.api.v1.category_routes import router as category_router
from app.api.v1.product_routes import router as product_router

app=FastAPI()

init_db()

app.include_router(category_router)
app.include_router(product_router)