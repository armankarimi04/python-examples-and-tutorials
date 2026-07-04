from typing import AsyncIterator
import anyio
from fastapi import FastAPI
import httpx
import pytest

app = FastAPI()

@app.get("/")
async def home():
    return {'message': "Hello World"}


# we need to tell pytest that we only want one backend, to fix the 'trio' error
# another option is to just install trio: pip install trio
# also setting @pytset.mark.asyncio on tests may work + pip install pytest-asyncio + import pytest_asyncio (or @pytest_asyncio.fixture)
# using httpx seems good (fastapi's TestClient uses httpx), just have to fix the version
@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


@pytest.fixture()
async def client() -> AsyncIterator[httpx.AsyncClient]: # this does not work (version is too new, pretty sure)
    async with httpx.AsyncClient(app=app, base_url='http://testserver') as client:
        yield client


@pytest.mark.anyio
async def test_home(client: httpx.AsyncClient) -> None:
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': "hi"}
    

# to test websockets endpoints, take a look at httpx-ws