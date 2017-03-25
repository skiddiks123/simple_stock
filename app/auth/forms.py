from flask_wtf import FlaskForm as Form
from wtforms import TextField, PasswordField, validators, SubmitField, IntegerField, BooleanField
from wtforms.validators import Required, Email, EqualTo
from app.models.user import User


class LoginForm(Form):
    email = TextField('Email Address', [Email(), Required(message='Forgot your email address?')])
    password = PasswordField('Password', [Required(message='Must provide a password. ;-)')])
    remember_me = BooleanField('Keep me logged in')

