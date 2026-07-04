import pytest
from httpx import AsyncClient
from app import app

BASE_URL = 'http://api:8000/latest/'

@pytest.fixture(scope='session')
async def test_async_client():
    """Fixture to get Test client for asynchronous tests"""
    async with AsyncClient(app=app, base_url=BASE_URL) as client:
        await app.router.startup()
        yield client
        await app.router.shutdown()
        
   
# Subscribe to 'user' channel
@pytest.mark.asyncio
@pytest.mark.order(1) # this test should be executed first
async def test_subscribe(test_async_client):
    response = await test_async_client.post(
        "subscribe/user"
    )
    
    pytest.SUBSCRIPTION_ID = response.json()['id'] # we assign SUBSCRIPTION_ID to pytest, so that if we needed it later in other tests, it can be accessed (like a global variable)
    assert response.status_code == 200
    
  
# Create 'listen' task handler  
import asyncio
def create_listen_task(test_async_client, subscription_id): # this should be used as a background service
    listen_path = '/'.join(['listen', str(subscription_id)])
    task_listen = asyncio.create_task(
        test_async_client.get(
            listen_path,
        )
    )
    return task_listen


# complete test example of this whole workflow
# Create a user & Receive an event (the user created event)
@pytest.mark.dependency(depends=['test_subscribe']) # test depends on another test, if that test fails, this test will be skipped
async def test_pipeline(test_async_client):
    task_listen = create_listen_task(test_async_client, pytest.SUBSCRIPTION_ID)
    
    user = {'username': "kernelci", 'password': "test"}
    response = await test_async_client.post(
        "/user",
        data=user
    )
    
    await task_listen
    event_data = get_event_data(task_listen.result()) # i don't know this one ??
    assert event_data.get('op') == 'created'
    assert event_data.get('id') == response.json()['id']
    
    
# Unsubscribe channel
@pytest.mark.dependency(depends=['test_subscribe'])
@pytest.mark.asyncio
@pytest.mark.order("last") # this test will be executed at the end
async def test_unsubscribe(test_async_client):
    response = await test_async_client.post(
        f"unsubscribe/{pytest.SUBSCRIPTION_ID}"
    )
    
    assert response.status_code == 200
    