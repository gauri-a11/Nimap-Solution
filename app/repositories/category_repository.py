from sqlalchemy.orm import Session
from app.models.category import Category

class CategoryRepository:

    def get_all(self,db:Session,skip:int,limit:int):
        return db.query(Category).offset(skip).limit(limit).all()

    def get_by_id(self,db:Session,id:int):
        return db.query(Category).filter(Category.id==id).first()

    def create(self,db:Session,data):
        category=Category(**data.dict())
        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    def update(self,db:Session,id:int,data):
        category=self.get_by_id(db,id)
        for key,value in data.dict().items():
            setattr(category,key,value)
        db.commit()
        db.refresh(category)
        return category

    def delete(self,db:Session,id: int):
        category=self.get_by_id(db,id)
        db.delete(category)
        db.commit()