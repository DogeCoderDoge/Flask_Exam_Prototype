from flask import Flask, render_template, url_for, redirect, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, RadioField, StringField, PasswordField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = '0xa520f079d17f785b7c4b42de25d24ebd'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False

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

'''
with app.app_context():
    db.drop_all()
    db.create_all()
    q1 = Question(content="question one", answer="this is the first option")
    q2 = Question(content="question two", answer="fourth")
    opt1 = Option(content="this is the first option", question=q1)
    opt2 = Option(content="second", question=q1)
    opt3 = Option(content="third", question=q2)
    opt4 = Option(content="fourth", question=q2)
    db.session.add_all([q1,q2,opt1,opt2,opt3,opt4])
    db.session.commit()
'''

#FORMS
page = 0
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



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/exam', methods=['GET', 'POST'])
def exam():
    global page
    forms = []

    for q in Question.query.all():
        a,b = q.options
        form = QuestionForm(q.content, [a.content,b.content])
        forms.append(form)


    if page < Question.query.count():
        if forms[page].validate_on_submit():
            if request.form.get('options') == Question.query.all()[page].answer:
                print("correct")
            print("form submitted")
            page += 1

            return redirect(url_for('exam'))

        return render_template('exam.html', form=forms[page])

    else:
        return redirect(url_for('home'))


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
    