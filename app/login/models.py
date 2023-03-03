from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

@dataclass
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User {self.email}"


class Users(db.Model):
    __tablename__ = 'test'
    
    username: str = db.Column(db.String(255),primary_key=True)

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return f"User {self.username}"

