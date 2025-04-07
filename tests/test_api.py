# Test app

from src import app
from pytest import fixture

@fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/api')
    assert response.status_code == 200
    assert response.get_json() == {'message': 'You are now subscribed to our newsletter!.'}

def test_about(client):
    response = client.get('/api/subscribe')
    assert response.status_code == 200
    assert response.get_json() == ({
        "message": "You are now subscribed to our newsletter!."
    })
