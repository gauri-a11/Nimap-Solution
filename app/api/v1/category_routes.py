from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.db import get_db
from app.schemas.category_schema import CategoryCreate
from app.services.category_service import CategoryService

router=APIRouter(prefix="/api/categories")
service=CategoryService()

@router.get("/")
def get_categories(page:int=1,size:int=10,db:Session=Depends(get_db)):
    return service.get_all(db,page,size)

@router.post("/")
def create_category(data:CategoryCreate,db:Session=Depends(get_db)):
    return service.create(db,data)

@router.get("/{id}")
def get_category(id:int,db:Session=Depends(get_db)):
    return service.get(db,id)

@router.put("/{id}")
def update_category(id:int,data:CategoryCreate,db:Session=Depends(get_db)):
    return service.update(db,id,data)

@router.delete("/{id}")
def delete_category(id:int,db:Session=Depends(get_db)):
    service.delete(db,id)
    return {"message":"Deleted"}