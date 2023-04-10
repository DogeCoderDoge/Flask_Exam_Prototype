from flask_sqlalchemy import SQLAlchemy
from Website.main import app
from flask_login import UserMixin

db = SQLAlchemy(app)

#DATABASE MODELS
class Question(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))
    options = db.relationship('Option', backref='question')
    answer = db.Column(db.String(100))

class Option(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(25))
    question_id = db.Column(db.Integer, db.ForeignKey('question._id'))

class User(db.Model, UserMixin):
    _id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(5))
    password = db.Column(db.String(10))
    marks = db.Column(db.Integer)

    def get_id(self):
        return self._id

