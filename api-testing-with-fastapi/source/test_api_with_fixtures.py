import pytest
from sqlalchemy.orm import Session
from typing import Generator
from main_with_dependecy import Base, engine, DBItem
from test_api_with_setup_and_teardown import TestingSessionLocal

# Instead of setup and teardown functiosn we could have pytest fixtures


@pytest.fixture
def session() -> Generator[Session, None, None]:
    Base.metadata.create_all(bind=engine)
    
    db_session = TestingSessionLocal()
    db_item = DBItem(id=100, name="Test Item", description="This is a test item")
    session.add(db_item)
    session.commit()
    session.close()
    
    yield db_session
    
    db_session.close()
    Base.metadata.drop_all(bind=engine)
    
    
def test_create_item(session: Session) -> None:
    # omitted
    pass