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
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    user = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, pubname, description, latitude, longitude, user):
        self.pubname = pubname
        self.description = description
        self.latitude = latitude
        self.longitude = longitude
        self.user = user

