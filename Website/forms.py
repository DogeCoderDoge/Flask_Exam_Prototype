from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, StringField, PasswordField, validators

class QuestionForm(FlaskForm):
    question = StringField()
    options = RadioField()
    submit = SubmitField('Submit')

    def __init__(self, q, opt):
        super().__init__()
        self.question.label = q
        self.options.choices = opt


class LoginForm(FlaskForm):
    userID = StringField('User ID', validators=[])
    password = PasswordField('Password')
    submit = SubmitField('Login')

