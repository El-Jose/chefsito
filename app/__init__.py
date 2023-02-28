from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

from app.login.views import login
app.register_blueprint(login)
db.create_all()
