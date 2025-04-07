from dataclasses import dataclass
from src import app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

# Define a model (Table) for the database
@dataclass
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), unique=False, nullable=False)
    last_name = db.Column(db.String(100), unique=False, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Store hashed passwords
    is_admin = db.Column(db.Boolean, default=False, nullable=False)  # Admin flag

    def __repr__(self):
        return f'<User {self.username}>'
    
    id: str
    first_name: str
    last_name: str
    username: str
    email: str
    is_admin: str

# Create the database tables (if they don't exist)
with app.app_context():
    db.create_all()

