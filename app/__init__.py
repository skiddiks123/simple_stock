from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

db = SQLAlchemy(app)
db.init_app(app)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.singin'
login_manager.init_app(app)

# Добавления файла конфигурации 
app.config.from_object('config')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

from app.home.controllers import home as home_module
from app.auth.controllers import auth as auth_module


app.register_blueprint(home_module)
app.register_blueprint(auth_module)



# Импорт моделей 
from app.models.user import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))