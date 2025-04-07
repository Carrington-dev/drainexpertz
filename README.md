# Adventures
A traveling agency in South Africa to the world 

```bash
https://www.thriftyadventures.co.za/pages/about-us
```
## 

To **test your Flask app**, you should write **unit tests** using `pytest` and `Flask's test client`. This ensures that your routes, authentication, and security features work as expected.

---

## **1. Install `pytest`**
If you haven't installed `pytest`, run:  
```bash
pip install pytest
```

---

## **2. Create a `tests/` Directory**
Inside your project, create a `tests/` folder:

```
/your_project
    /static
    /templates
    /tests
        __init__.py
        test_app.py
    app.py
```

---

## **3. Write Unit Tests in `tests/test_app.py`**
Create `test_app.py` inside the `tests/` folder.

```python
import pytest
from app import app, db, User
from flask import url_for
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@pytest.fixture
def client():
    """Set up a test client and an empty database."""
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Use in-memory DB for tests
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_home_page(client):
    """Test if the home page loads correctly."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_register(client):
    """Test user registration."""
    response = client.post("/register", data={
        "username": "testuser",
        "password": "password123",
        "confirm_password": "password123"
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Account created" in response.data  # Flash message confirmation

    # Check if user exists in the database
    with app.app_context():
        user = User.query.filter_by(username="testuser").first()
        assert user is not None

def test_login(client):
    """Test user login."""
    # Create a test user in the database
    with app.app_context():
        hashed_password = bcrypt.generate_password_hash("password123").decode("utf-8")
        test_user = User(username="testuser", password=hashed_password)
        db.session.add(test_user)
        db.session.commit()

    response = client.post("/login", data={
        "username": "testuser",
        "password": "password123"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Dashboard" in response.data  # Should redirect to dashboard

def test_logout(client):
    """Test if logout works properly."""
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"Logged out successfully" in response.data

def test_protected_dashboard(client):
    """Test access to a protected page without login."""
    response = client.get("/dashboard", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data  # Should redirect to login page

```

```bash
sudo ln -s /home/ubuntu/adventures/settings/gunicorn.socket /etc/systemd/system/gunicorn.socket
sudo ln -s /home/ubuntu/adventures/settings/gunicorn.service /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn
sudo systemctl enable gunicorn

sudo ln -s /home/ubuntu/adventures/settings/ad.conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/ad.conf /etc/nginx/sites-enabled

```
```bash
https://roadtrippers.co.za/contact-us/
https://www.thriftyadventures.co.za/pages/contact
https://www.roadtravel.co.za/
sudo certbot --nginx -d ad.vroomhive.co.zw -d www.ad.vroomhive.co.zw
https://github.com/flasgger/flasgger
```

---

## **4. Run Tests**
Run your tests using:
```bash
pytest tests/
pytest
```

This will check:
✅ Home page loads correctly  
✅ User registration works  
✅ User login works  
✅ Logout functions correctly  
✅ Dashboard is protected and redirects to login  

<!-- Would you like to add **integration tests, API testing, or security penetration testing**? 🚀 -->
```bash
@app.route("/api/users")
def get_all_users():
    """
    Get all users
    ---
    tags:
      - Users
    responses:
      200:
        description: A list of all users
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              username:
                type: string
                example: johndoe
              email:
                type: string
                example: johndoe@example.com
    """
    users = User.query.all()  # Query all users from the database
    return users

```