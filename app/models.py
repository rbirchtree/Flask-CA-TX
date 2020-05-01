from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64), index=True, unique=True)
    phonenumber=db.Column(db.String(64), index=True, unique=True)
    notes=db.Column(db.String(256), index=True)
    email=db.Column(db.String(128), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)  
    
