from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from .main_with_dependecy import app, get_db, Base, DBItem

DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    DATABASE_URL, 
    connect_args={
        "check_same_thread": False
    }, 
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

client = TestClient(app)

# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

def override_get_db():
    database = TestingSessionLocal()
    yield database
    database.close()

        
app.dependency_overrides[get_db] = override_get_db # this will replace the original database with test database in memory


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Server is running..."
    
    
def setup():
    Base.metadata.create_all(bind=engine)
    
    # a sample item
    session = TestingSessionLocal()
    db_item = DBItem(id=100, name="Test Item", description="This is a test item")
    session.add(db_item)
    session.commit()
    session.close()
    
    
def teardown():
    Base.metadata.drop_all(bind=engine)
    

def test_read_item():
    item_id = 100
    response = client.get(f'/items/{item_id}')
    assert response.status_code == 200, response.text # ?
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["description"] == "This is a test item"
    assert data["id"] == item_id