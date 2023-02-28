from flask import request, jsonify, Blueprint 
from app import db 
from app.login.models import User 
 
login = Blueprint('login', __name__)
 
@login.route('/login')
def login_post(): 
    return "Welcome to the Login module."