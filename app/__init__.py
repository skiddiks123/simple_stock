from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

db = SQLAlchemy(app)
db.init_app(app)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Добавления файла конфигурации 
config = app.config.from_object('config')

from app.home.controllers import home as home_module

from app.models import user
app.register_blueprint(home_module)