from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient

from app import app
from database import get_db

client = TestClient(app=app)

DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "check_same_thread": False,
    },
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to override the get_db dependency in the main app
def override_get_db():
    database = TestingSessionLocal()
    yield database
    database.close()
    
app.dependency_overrides[get_db] = override_get_db