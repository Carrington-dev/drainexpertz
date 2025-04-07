import pytest
import json
from src import app, db, User

@pytest.fixture
def client():
    """Setup a test client and test database"""
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = "SECRET_KEY"

    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memory.db'  # Using SQLite

    client = app.test_client()

    with app.app_context():
        db.create_all()
        yield client  # Tests run here
        db.drop_all()  # Cleanup after tests

def test_create_user_success(client):
    """Test successful user creation"""
    response = client.post('/api/users', 
                           data=json.dumps({
                            "email": "johndoe2@example.com",
                            "first_name": "Maanda",
                            "is_admin": False,
                            "last_name": "Muleya",
                            "password": "#Maanda2",
                            "username": "johndoe2"
                            }),
                           content_type='application/json')

    assert response.status_code == 201
    assert b'Maanda' in response.data

def test_create_user_duplicate(client):
    """Test creating a duplicate user"""
    client.post('/api/users', 
                data=json.dumps({
                            "email": "johndoe2@example.com",
                            "first_name": "Maanda",
                            "is_admin": False,
                            "last_name": "Muleya",
                            "password": "#Maanda2",
                            "username": "johndoe2"
                            }),
                content_type='application/json')

    response = client.post('/api/users', 
                           data=json.dumps({
                            "email": "johndoe2@example.com",
                            "first_name": "Maanda",
                            "is_admin": False,
                            "last_name": "Muleya",
                            "password": "#Maanda2",
                            "username": "johndoe2"
                            }),
                           content_type='application/json')

    assert response.status_code == 400
    assert b'exists' in response.data

def test_create_user_invalid_data(client):
    """Test missing username"""
    response = client.post('/api/users', 
                           data=json.dumps({
                            "email": "johndoe2@example.com",
                            "first_name": "Maanda",
                            "is_admin": False,
                            "last_name": "Muleya",
                            "password": "#Maanda2",
                            # "username": "johndoe2"
                            }),
                           content_type='application/json')

    assert response.status_code == 400
    assert b'required' in response.data
