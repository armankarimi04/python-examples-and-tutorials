import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock
from app import app

BASE_URL = f'http://testserver/'

@pytest.fixture
def test_client():
    """Fixture to get FastAPI Test client instance"""
    with TestClient(app=app, base_url=BASE_URL) as client:
        return client
    
@pytest.fixture
def mock_init_sub_id(mocker):
    async_mock = AsyncMock()
    mocker.patch('api.pubsub.PubSub._init_sub_id', side_effect=async_mock) # i have no idea what is this trying to mock
    return async_mock
    
def test_root_endpoint(mock_init_sub_id, test_client):
    response = test_client.get('/')
    print("response.json()", response.json())
    assert response.status_code == 200
    assert response.json() == {'message': "KernelCI API"}
    
