from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Pub(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pubname = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=False)

    def __init__(self, pubname, description):
        self.pubname = pubname
        self.description = description
