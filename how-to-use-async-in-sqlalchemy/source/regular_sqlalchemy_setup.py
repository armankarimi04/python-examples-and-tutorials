from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///db.sqlite3", connect_args={'check_same_thread': False}) # check_same_thread is only required for sqlite and fastapi
SessionLocal = sessionmaker(engine)
Base = declarative_base() # allows to convert regular python classes to sqlalchemy models

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    
Base.metadata.create_all(engine) # will create the models in database

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# Pydantic
class UserBase(BaseModel):
    username: str
        
        
app = FastAPI()


@app.post("/user")
def index(user: UserBase, db: Session = Depends(get_db)):
    db_user = User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user) # we refresh to put the extra information in the object after creation, such as id
    return db_user

@app.get("/user")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return {'users': users}