from flask import Flask

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False
app.config['SECRET_KEY'] = '0xa520f079d17f785b7c4b42de25d24ebd'