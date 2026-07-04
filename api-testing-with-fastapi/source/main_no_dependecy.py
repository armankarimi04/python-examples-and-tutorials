from typing import Optional
from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str]
    
    
class ItemCreate(BaseModel):
    name: str
    description: Optional[str]
    

class ItemUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    
    
DATABASE_URL = "sqlite:///test.db"


class Base(DeclarativeBase):
    pass

class DBItem(Base):
    __tablename__ = "items"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[int] = mapped_column(String(30))
    description = Mapped[Optional[str]]
    
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)
    
@app.get("/")
def read_root():
    return "Server is running..."


# endpoint without Database dependecy (a session must be created)
@app.post("items")
def create_item(item: ItemCreate) -> Item:
    db = SessionLocal()
    db_item = DBItem(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return Item(**db_item.__dict__)
