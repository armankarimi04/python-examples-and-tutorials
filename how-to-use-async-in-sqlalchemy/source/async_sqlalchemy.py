from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

engine = create_async_engine("sqlite+aiosqlite:///db.sqlite3", connect_args={'check_same_thread': False}) # check_same_thread is only required for sqlite and fastapi
SessionLocal = async_sessionmaker(engine)
# Base = declarative_base() # allows to convert regular python classes to sqlalchemy models

class Base(DeclarativeBase): # sqlalchemy 2.0 (which supports async) changed the way queries run, and how models are defined
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    

# IMPORTANT
# In async mode, we can't just call Base.metadata.create_all(engine) here.
# It needs to be in an event loop.
# so we comment it out. and put it in get_db (and also update get_db)
# Base.metadata.create_all(engine) # will create the models in database

async def get_db(): # now this will only get called when get_db is called, and get_db is called only when one of the endpoints is called
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) # this will call Base.metadata.create_all synchronously (required to be async)
        
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()
        
        
# Pydantic
class UserBase(BaseModel):
    username: str
        
        
app = FastAPI()


@app.post("/user")
async def index(user: UserBase, db: AsyncSession = Depends(get_db)):
    db_user = User(username=user.username)
    db.add(db_user)
    await db.commit() # creating and adding user to session do not require await, but as soon as we attempt to touch the database we need to await it
    await db.refresh(db_user) # we refresh to put the extra information in the object after creation, such as id
    return db_user


# in sqlalchemy 2.0, the way queries are made is updated
@app.get("/user")
async def get_users(db: AsyncSession = Depends(get_db)):
    # users = db.query(User).all()
    results = await db.execute(select(User))
    users = results.scalars().all()
    return {'users': users}


# summary:
# async driver
# async functions
# await anything that touches database
# convert queries to the new style