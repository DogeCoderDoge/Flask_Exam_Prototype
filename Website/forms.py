from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, StringField, PasswordField

class QuestionForm(FlaskForm):
    question = StringField()
    options = RadioField()
    submit = SubmitField('Submit')

    def __init__(self, q, opt):
        super().__init__()
        self.question.label = q
        self.options.choices = opt


class LoginForm(FlaskForm):
    userID = StringField('User ID')
    password = PasswordField('Password')
    submit = SubmitField('Login')

