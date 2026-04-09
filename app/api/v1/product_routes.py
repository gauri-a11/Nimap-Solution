from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.schemas.product_schema import ProductCreate
from app.services.product_service import ProductService

router=APIRouter(prefix="/api/products")
service=ProductService()

@router.get("/")
def get_products(page:int=1,size:int=10,db:Session=Depends(get_db)):
    return service.get_all(db,page,size)

@router.post("/")
def create_product(data:ProductCreate,db:Session=Depends(get_db)):
    return service.create(db,data)

@router.get("/{id}")
def get_product(id:int,db:Session=Depends(get_db)):
    return service.get(db,id)

@router.put("/{id}")
def update_product(id:int,data:ProductCreate,db:Session=Depends(get_db)):
    return service.update(db,id,data)

@router.delete("/{id}")
def delete_product(id:int,db:Session=Depends(get_db)):
    service.delete(db,id)
    return {"message":"Deleted"}