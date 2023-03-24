from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

@dataclass
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    temp_num = db.Column(db.Integer)

    def __init__(self, email, password):
        self.email = email
        self.password = password
        #self.temp_num = temp_num

    def __repr__(self):
        return f"User {self.email}"


class Users(db.Model):
    __tablename__ = 'test'
    
    username: str = db.Column(db.String(255),primary_key=True)

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return f"User {self.username}"

