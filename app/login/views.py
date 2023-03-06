
from flask import Flask, request, jsonify, Blueprint, abort
from werkzeug.security import generate_password_hash, check_password_hash

from app.login.models import User, Users, db

login = Blueprint('login', __name__)


@login.route('/login', methods=['POST'])
def login_view():
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            return jsonify('contraseña correcta')
        else:
            return abort(501, description="error trying to login")
    return jsonify('login successful!')


@login.route('/register', methods=['POST'])
def register_view():
    if request.method == 'POST':
        try:
            email = request.json['email']
            password = request.json['password']
            user = User(email=email, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return abort(501, description=f"error trying to register: {e}")
        return jsonify('register successful')
