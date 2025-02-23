from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(100))
    date = db.Column(db.String(100))
    subject = db.Column(db.String(100))
    pupil = db.Column(db.String(100))
    place = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    lessons = db.relationship('Lesson')

