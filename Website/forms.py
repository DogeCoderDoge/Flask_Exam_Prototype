from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, StringField, PasswordField, validators
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    question = StringField()
    options = RadioField(validators=[DataRequired()])
    submit = SubmitField('Submit')

    def __init__(self, q, opt):
        super().__init__()
        self.question.label = q
        self.options.choices = opt


class LoginForm(FlaskForm):
    userID = StringField('User ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

