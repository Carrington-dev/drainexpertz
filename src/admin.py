from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from src import app, User, db

admin = Admin(app, name='Admin Panel', template_mode='bootstrap4')

admin.add_view(ModelView(User, db.session))
