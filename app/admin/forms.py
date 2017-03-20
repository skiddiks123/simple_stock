from flask_wtf import FlaskForm as Form
from wtforms import TextField, PasswordField, validators, SubmitField, IntegerField, BooleanField
from wtforms.validators import Required, Email, EqualTo
from app.models.user import User

class SignupForm(Form):
    nickname = TextField("nickname",  [validators.Required("Please enter your first name.")])
    email = TextField("email",  [validators.Required(
        "Please enter your email address."), validators.Email("Please enter your email address.")])
    password = PasswordField(
        'password', [validators.Required("Please enter a password.")])
   
    submit = SubmitField("Create account")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False
        else:
            return True
