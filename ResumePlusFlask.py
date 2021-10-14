import os
import os  # os is used to get environment variables IP & PORT
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template
from flask import request, Response
from flask import redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

from database import db
from models import User as User
from forms import RegisterForm, LoginForm
import bcrypt

app = Flask(__name__)  # create an app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resumeplus_flask_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'SE3155'

db.init_app(app)
with app.app_context():
    db.create_all() # run under the app context

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if session.get('user'):
        return render_template('ResumePlusHomePage.html', user=session['user'])
    return redirect(url_for('login'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    register_form = RegisterForm()
    if request.method == 'POST' and register_form.validate_on_submit():
        h_password = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
        username = request.form['username']
        new_user = User(username, h_password)
        db.session.add(new_user)
        db.session.commit()
        session['user'] = username
        session['user_id'] = new_user.id
        return redirect(url_for('home_page'))
    return render_template('ResumePlusRegister.html', form=register_form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    if request.method == 'POST' and login_form.validate_on_submit():
        the_user = db.session.query(User).filter_by(username=request.form['username']).one_or_none()
        if the_user == None:
            return render_template('ResumePlusLogin.html', form=login_form)
        if bcrypt.checkpw(request.form['password'].encode('utf-8'), the_user.password):
            session['user'] = the_user.username
            session['user_id'] = the_user.id
            return redirect(url_for('home_page'))

        login_form.password.errors = ["Incorrect username or password"]
        return render_template('ResumePlusLogin.html', form=login_form)
    else:
        return render_template('ResumePlusLogin.html', form=login_form)

@app.route('/home_page')
def home_page():
    if session.get('user'):
        return render_template('ResumePlusHomePage.html', user=session['user'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    if session.get('user'):
        session.clear()
    return redirect(url_for('login'))

app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)

# T
# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000