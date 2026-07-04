from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from schemas import ProductCreate
from database import get_db, Product


app = FastAPI()

@app.post("/products/")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(name=product.name, description=product.description)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product