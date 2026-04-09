from sqlalchemy.orm import Session
from app.models.product import Product

class ProductRepository:

    def get_all(self,db:Session,skip:int,limit:int):
        return db.query(Product).offset(skip).limit(limit).all()

    def get_by_id(self,db:Session,id:int):
        return db.query(Product).filter(Product.id==id).first()

    def create(self,db:Session,data):
        product=Product(**data.dict())
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def update(self,db:Session,id:int,data):
        product=self.get_by_id(db,id)
        for key,value in data.dict().items():
            setattr(product,key,value)
        db.commit()
        db.refresh(product)
        return product

    def delete(self,db:Session,id: int):
        product=self.get_by_id(db,id)
        db.delete(product)
        db.commit()