
import secrets

from flask import Blueprint, Flask, abort, current_app, jsonify, request, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from app.login.models import User, db

login = Blueprint('login', __name__)
# ______________________________________________________________________________


@login.route('/login', methods=['POST'])
def login_view():
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']
        user = User.query.filter_by(email=email).first()
        hash_password = user.password
        if user and check_password_hash(hash_password, password):
            return jsonify('correct password')
        else:
            return abort(501, description="error trying to login")
    return jsonify('login successful!')
# ______________________________________________________________________________


@login.route('/register', methods=['POST'])
def register_view():
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password']
        if User.query.filter_by(email=email).first():
            return abort(409, description="error to register")
        try:
            user = User(email=email, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return abort(501, description=f"error trying to register: {e}")
        return jsonify('register successful')
# ______________________________________________________________________________


@login.route('/recovery', methods=['POST'])
def password_recovery():
    if request.method == 'POST':
        email = request.json['email']
        user = User.query.filter_by(email=email).first()
        if user:
            codigo = str(secrets.randbelow(1000000)).zfill(6)
            user.temp_num = codigo
            db.session.add(user)
            db.session.commit()# aca no hace el commit a la bd
            return jsonify({'codigo': codigo})
    return jsonify({'mensaje': 'Correo electrónico no encontrado'})
# ______________________________________________________________________________


@login.route('/reset', methods=['POST'])
def passord_reset():
    import pdb; pdb.set_trace()
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        codigo = int(data.get('codigo'))
        user = User.query.filter_by(email=email).first()
        if user and user.temp_num == codigo:
            pswrd = data.get('password')
            confirm_password = data.get('confirm')
            if pswrd == confirm_password:
                # Actualizar la contraseña del usuario
                pswrd1 = generate_password_hash(pswrd)
                user.password = pswrd1
                user.temp_num = None
                db.session.commit()
                return jsonify({'La contraseña se ha actualizado correctamente':'success'})
            else:
                return jsonify({'message': 'Las contraseñas no coinciden'}), 400
        else:
            return jsonify({'message': 'El correo electrónico o el código son incorrectos'}), 400
# ______________________________________________________________________________
