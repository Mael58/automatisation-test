import pytest
from app import app as befe

@pytest.fixture
def app():
    befe.config.update(
        {
            'TESTING': True
        }
    )
    return befe

@pytest.fixture
def client(app):
    return app.test_client()

def test_request_index(client):
    response = client.get('/')
    assert b'Welcome to ze BEFE' in response.data

