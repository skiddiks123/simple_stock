from flask import Blueprint, render_template
from app import decorators

home = Blueprint('home', __name__, url_prefix='/')


@home.route('/')
@decorators.login_required
def index():
    return render_template('/home/index.html')