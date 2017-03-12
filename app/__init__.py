from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy(app)
db.init_app(app)

@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('auth.signin'))

# Добавления файла конфигурации 
app.config.from_object('config')

from app.home.controllers import home as home_module
from app.mod_auth.controllers import mod_auth as auth_module
# Импорт моделей 
from app.models import user

app.register_blueprint(home_module)
app.register_blueprint(auth_module)