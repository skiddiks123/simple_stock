from app import db, login_manager
from werkzeug import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(64), index=True, unique=True)
    lname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(192),  nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % (self.uname)

    def __init__(self, uname, email, password):
        self.uname = uname.title()
        self.email = email.lower()
        self.password = password


