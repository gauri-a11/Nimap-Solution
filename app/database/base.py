from sqlalchemy.orm import declarative_base

Base=declarative_base()

from app.models.category import Category
from app.models.product import Product