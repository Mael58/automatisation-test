import pytest
from eventfrontservice.app import app as befe

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
                    "price": 0
                },
                {
                    "event_id": 2,
                    "event_title": "event 2",
                    "is_free": True,
                    "already_registered": True,
                    "price": 0
                },
                {
                    "event_id": 3,
                    "event_title": "event 3",
                    "is_free": False,
                    "already_registered": False,
                    "price": 421
                },
                {
                    "event_id": 4,
                    "event_title": "event 4",
                    "is_free": False,
                    "already_registered": True,
                    "price": 102
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

@pytest.mark.parametrize("event_title,is_free", [('event is free', True), ('event is not free', False)])
def test_new_event_free(client, event_title, is_free):
    response = client.post('/event', data = {
        'event_title': event_title,
        'is_free': is_free
    })
    assert response.status_code == 302
    response_events = client.get('/events')
    assert response_events.status_code == 200
    assert event_title.encode() in response_events.data

def test_new_event_missing_event_title(client):
    response = client.post('/event', data = {
        'is_free': False
    })
    assert response.status_code == 400
    assert b'missing event title' in response.data


def test_subscribe_event_not_free(client, mocker):
    mocker.patch('grpc.insecure_channel')
    response = client.post('/event/3/subscribe', data = {
        'price': 200.2,
        'card_id': 120,
        'event_id': 3,
        'user_id': 12        
    })
    assert response.status_code == 200
    assert b'event 3' in response.data
    assert b'Payment refused' not in response.data

def test_subscribe_event_not_free_payment_refused(client, mocker):
    mocker.patch('grpc.insecure_channel') #FIXME
    response = client.post('/event/3/subscribe', data = {
        'price': 200.2,
        'card_id': 120,
        'event_id': 3,
        'user_id': 12        
    })
    assert response.status_code == 200
    assert b'event 3' in response.data
    assert b'Payment refused' in response.data