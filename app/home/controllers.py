from flask import Blueprint, render_template
from app import decorators
from flask_login import login_required, current_user
from app.models.user import User

home = Blueprint('home', __name__,)

@home.route('/')
@home.route('/home')
@home.route('/index')
@decorators.login_required
def index():
    user = current_user.nickname
    return render_template('home/index.html', user = user)