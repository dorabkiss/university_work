from flask_sqlalchemy import SQLAlchemy
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import os
import base64
import hashlib

# we are using the second of flask-sqlalchemy's configuration options
# which is to create the sqlalchemy object here and bind it to the app once the
# app is initialised

db = SQLAlchemy()

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50))
    hashed = db.Column(db.String(150))
    salt = db.Column(db.String(150))
    twits = db.relationship('Twits',backref='user', lazy=True)

    def get_salt(self):
        self.salt = base64.b64encode(os.urandom(20))

    def get_hash(self, plain):
        self.hashed = hashlib.sha512(self.salt+(plain.encode('utf-8'))).hexdigest()

    # these are the user model attributes required by Flask-Login
    def get_id(self):
        return self.user_id

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

class Twits(db.Model):

    twit_id = db.Column(db.Integer, primary_key = True)
    twit = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return self.twit
