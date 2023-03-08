
from flask import Flask

from app.login.models import db
from app.login.views import login

def create_app(config_filename=None):
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        app.register_blueprint(login)
        db.init_app(app)
        db.app = app
        db.create_all()