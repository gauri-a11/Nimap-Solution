from pydantic import BaseModel
from app.schemas.category_schema import CategoryResponse

class ProductBase(BaseModel):
    name:str
    category_id:int

class ProductCreate(ProductBase):
    pass

class ProductResponse(BaseModel):
    id:int
    name:str
    category:CategoryResponse

    class Config:
        orm_mode=True