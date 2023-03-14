
from flask import Flask

from app.login.models import db
from app.login.views import login


current_app = Flask(__name__)
current_app.config.from_object('config.Config')

with current_app.app_context():
    current_app.register_blueprint(login)
    db.init_app(current_app)
    db.app = current_app
    db.create_all()