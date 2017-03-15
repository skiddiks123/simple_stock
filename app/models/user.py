from app import db, login_manager
from werkzeug import check_password_hash, generate_password_hash
from flask_login import UserMixin
ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(192),  nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    def __init__(self, nickname, email, password):
        self.nickname = nickname.title()
        self.email = email.lower()
        self.password = password


