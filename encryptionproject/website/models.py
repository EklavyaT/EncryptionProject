from website import db
from flask_login import UserMixin




class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(320),unique=True)
    password=db.Column(db.String(50))
    username=db.Column(db.String(16))
    


    
