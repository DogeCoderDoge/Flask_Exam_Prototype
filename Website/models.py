from flask_sqlalchemy import SQLAlchemy
from Website.main import app

db = SQLAlchemy(app)

#DATABASE MODELS
class Question(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100))
    options = db.relationship('Option', backref='question', lazy=True)
    answer = db.Column(db.String(100))

class Option(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(25))
    question_id = db.Column(db.Integer, db.ForeignKey('question._id'))
    