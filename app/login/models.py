from app import db 
 
class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    email = db.Column(db.String(255)) 
    password = db.Column(db.String(255)) 
 
    def __init__(self, email, password):
        self.email = email
        self.password = password
 
    def __repr__(self): 
        return f"User {self.email}"