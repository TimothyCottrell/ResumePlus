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
bcryptCode = 'utf-8'

db.init_app(app)
with app.app_context():
    db.create_all() # run under the app context

@app.route('/')
@app.route('/index')
def landing():
    if session.get('user'):
        return redirect(url_for('home_page'))
    return render_template('Landing.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        # for i in request.form:
        #     print(str(i) + ": " + str(request.form[i]))
        h_password = bcrypt.hashpw(request.form['password'].encode(bcryptCode), bcrypt.gensalt())
        username = request.form['username']
        new_user = User(username, h_password)
        db.session.add(new_user)
        db.session.commit()
        session['user'] = username
        session['user_id'] = new_user.id
        return redirect(url_for('home_page'))
    return render_template('Register.html')

@app.route('/home_page')
def home_page():
    if session.get('user'):
        return render_template('Home.html', user=session['user'])
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # for i in request.form:
        #     print(str(i) + ": " + str(request.form[i]))
        the_user = db.session.query(User).filter_by(username=request.form['username']).one_or_none()
        if the_user == None:
            return render_template('Login.html')
        if bcrypt.checkpw(request.form['password'].encode(bcryptCode), the_user.password):
            session['user'] = the_user.username
            session['user_id'] = the_user.id
            return redirect(url_for('home_page'))
        return render_template('Login.html')
    else:
        return render_template('Login.html')

@app.route('/logout')
def logout():
    if session.get('user'):
        session.clear()
    return redirect(url_for('login'))

app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)

# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000