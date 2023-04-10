from Website.main import app
from Website.forms import LoginForm, QuestionForm
from Website.models import Question, Option, User, db
from flask import render_template, url_for, redirect, request, flash
from flask_login import logout_user, login_user, login_required, LoginManager, current_user

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

'''
with app.app_context():
    db.drop_all()
    db.create_all()

    q1 = Question(content="question one", answer="this is the first option")
    q2 = Question(content="question two", answer="fourth")
    q3 = Question(content="answer is dog", answer="dog")

    opt1 = Option(content="this is the first option", question=q1)
    opt2 = Option(content="second", question=q1)
    opt3 = Option(content="third", question=q2)
    opt4 = Option(content="fourth", question=q2)
    opt5 = Option(content="dog", question=q3)
    opt6 = Option(content="cat", question=q3)

    u1 = User(userID='00001', password='Student123', marks=0)

    db.session.add_all([q1,q2,q3,opt1,opt2,opt3,opt4,opt5,opt6,u1])
    db.session.commit()
'''


@app.route('/')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if len( list( User.query.filter_by(    userID=request.form.get('userID')    ) ) ) > 0:
            user = User.query.filter_by(userID=request.form.get('userID')).first()

            if user.userID == request.form.get('userID') and user.password == request.form.get('password'):
                flash(f'You are logged in as {user.userID}!', 'success')
                login_user(user, remember=True)

                return redirect(url_for('home'))

            else: 
                flash('Wrong credentials!', 'danger')

        else:
            flash('Wrong credentials!', 'danger')
            return render_template('login.html', form=form)

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/exam/<int:page>', methods=['GET', 'POST'])
@login_required
def exam(page):
    q_list = Question.query.all()

    q = q_list[page-1]
    opt1, opt2 = q.options
    form = QuestionForm(q.content, [opt1.content, opt2.content])

    if page <= Question.query.count():
        print(page)

        if form.validate_on_submit():
            page += 1
            if request.form.get('options') == q.answer:
                pass #add some code for user's marks n stuff

            return redirect(url_for('exam', page=page))

        return render_template('exam.html', form=form)

    else:
        return redirect(url_for('home'))


'''    
@app.route('/add_user', methods=['GET','POST'])
def add_user():
    form = LoginForm()

    if form.validate_on_submit():
        user = User(userID=request.form.get('userID'), password=request.form.get('password'))
        db.session.add_all([user])
'''    

