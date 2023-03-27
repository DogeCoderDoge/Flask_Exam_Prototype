from Website.main import app
from Website.forms import LoginForm, QuestionForm
from Website.models import Question, Option, db
from flask import render_template, url_for, redirect, request


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

@app.route('/')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
    
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

    