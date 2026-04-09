from app.repositories.product_repository import ProductRepository

repo=ProductRepository()

class ProductService:

    def get_all(self,db,page,size):
        skip=(page-1)*size
        return repo.get_all(db,skip,size)

    def get(self,db,id):
        return repo.get_by_id(db,id)

    def create(self,db,data):
        return repo.create(db,data)

    def update(self,db,id,data):
        return repo.update(db,id,data)

    def delete(self,db,id):
        return repo.delete(db,id)