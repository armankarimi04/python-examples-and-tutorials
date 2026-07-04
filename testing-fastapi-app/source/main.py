from fastapi import FastAPI
import pytest
from fastapi.testclient import TestClient

app = FastAPI()

@app.on_event("startup")
def startup():
    # raise Exception("Something went wrong") # problem is that this won't run in testing, until we update our fixture to use context manager
    print("Starting...")

@app.get("/")
def home():
    return {'message': "hi"}


@pytest.fixture
def client():
    with TestClient(app) as _client:
        yield _client


def test_home(client: TestClient) -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": 'hi'}