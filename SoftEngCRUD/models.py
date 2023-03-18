from flask_sqlalchemy import SQLAlchemy
db =SQLAlchemy()
 
class UserModel(db.Model):
    __tablename__ = "users"
 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    score = db.Column(db.String())
 
    def __init__(self, first_name,last_name,score):
        self.first_name = first_name
        self.last_name = last_name
        self.score = score
 
    def __repr__(self):
        return f"{self.first_name}:{self.last_name}"