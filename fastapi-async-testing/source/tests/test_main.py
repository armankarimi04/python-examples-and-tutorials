import pytest
from fastapi.testclient import TestClient
from app import app

BASE_URL = f'http://testserver/'

@pytest.fixture
def test_client():
    """Fixture to get FastAPI Test client instance"""
    with TestClient(app=app, base_url=BASE_URL) as client:
        return client
    
def test_root_endpoint(test_client):
    response = test_client.get('/')
    print("response.json()", response.json())
    assert response.status_code == 200
    assert response.json() == {'message': "KernelCI API"}
    
# in the video, this test fails because it tries to connect to redis
# and pub-sub mechanism is implemented based on redis (publisher-subscribe mechanism in this project was implemented on redis)
# and redis is not available here, so the test fails, unless we mock it
# refer to test_main_with_pubsub_mock.py