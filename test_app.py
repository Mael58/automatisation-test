import pytest
from app import app as befe


@pytest.fixture
def app():
    befe.config.update(
        {
            "TESTING": True,
            "events": [
                {
                    "event_id": 1,
                    "event_title": "event 1",
                    "is_free": True,
                    "already_registered": False,
                },
                {
                    "event_id": 2,
                    "event_title": "event 2",
                    "is_free": True,
                    "already_registered": True,
                },
                {
                    "event_id": 3,
                    "event_title": "event 3",
                    "is_free": False,
                    "already_registered": False,
                },
                {
                    "event_id": 4,
                    "event_title": "event 4",
                    "is_free": False,
                    "already_registered": True,
                },
            ],
        }
    )
    return befe


@pytest.fixture
def client(app):
    return app.test_client()


def test_request_index(client):
    response = client.get("/")
    assert b"Welcome to ze BEFE" in response.data


@pytest.mark.parametrize("event_id", list(range(1, 5)))
def test_request_events(client, event_id):
    response = client.get("/events")
    assert "event {event_id}".format(event_id=event_id).encode() in response.data
