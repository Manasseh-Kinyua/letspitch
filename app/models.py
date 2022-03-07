from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))

class Pitch(db.model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(15000))
    date = (db.Column(timezone=True), default=func.now())
    user_id = db.column(db.Integer, db.ForeignKey('user.id'))


