import os  # os is used to get environment variables IP & PORT
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template
from flask import request, Response
from flask import redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop = stopwords.words('english')
import json
import bitstring

from database import db
from models import User
from models import Resume
from models import Text
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
        if db.session.query(User).filter_by(username=request.form['username']).count() == 0:
            # for i in request.form:
            #     print(str(i) + ": " + str(request.form[i]))
            h_password = bcrypt.hashpw(request.form['password'].encode(bcryptCode), bcrypt.gensalt())
            new_user = User(request.form['fname'], request.form['lname'], request.form['username'],
                            request.form['email'], h_password, False)
            db.session.add(new_user)
            db.session.commit()
            session['user'] = new_user.username
            session['email'] = new_user.email
            session['user_id'] = new_user.id
            return redirect(url_for('home_page'))
        else:
            # Insert case for if the username is already taken
            return render_template('Register.html')
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
        the_user = db.session.query(User).filter_by(email=request.form['username']).one_or_none()
        if the_user == None:
            the_user = db.session.query(User).filter_by(username=request.form['username']).one_or_none()
            if the_user == None:
                return render_template('Login.html')
        if bcrypt.checkpw(request.form['password'].encode(bcryptCode), the_user.password):
            session['user'] = the_user.username
            session['email'] = the_user.email
            session['user_id'] = the_user.id
            return redirect(url_for('home_page'))
        return render_template('Login.html')
    else:
        return render_template('Login.html')

@app.route('/account/settings')
def settings():
    the_user = db.session.query(User).filter_by(username=session.get('user')).one_or_none()
    if the_user:
        return render_template('Setting.html', user=the_user)
    return redirect(url_for('login'))

@app.route('/support')
def support():
    if session.get('user'):
        return render_template('Support.html', user=session['user'])
    return render_template('Support.html')

@app.route('/logout')
def logout():
    if session.get('user'):
        session.clear()
    return redirect(url_for('login'))

@app.route('/about')
def about():
    if session.get('user'):
        return render_template('About.html', user=session['user'])
    return render_template('About.html')

@app.route('/account/profile')
def profile():
    the_user = db.session.query(User).filter_by(username=session.get('user')).one_or_none()
    if the_user:
        return render_template('Profile.html', user=the_user)
    return redirect(url_for('login'))

@app.route('/save_resume', methods=['POST'])
def save_resume():
    data = json.loads(request.get_data())
    html = ''
    words = {}
    curHead = None
    for i in data:
        split = data[i]['text'].split()
        if len(split) > 0:
            for x in split:
                count = 0
                isHead = False
                head = curHead
                if not x in stop:
                    if x in words:
                        count = words[x]['count'] + 1
                    else:
                        count = 1
                        ht = data[i]['html']
                    if ht[1] == "h":
                        isHead = True
                        curHead = x
                    words[x] = {
                    "count" : count,
                    "isHead" : isHead,
                    "head" : head
                    }

        html += data[i]['html']
    bhtml = ''.join(format(x, 'b') for x in bytearray(html, 'utf-8'))
    the_user = db.session.query(User).filter_by(username=session.get('user')).one_or_none()
    new_resume = Resume(the_user.id, bitstring.BitArray(bin=bhtml).tobytes(),"testing")


    saved = bitstring.BitArray(bin=bhtml).tobytes()
    db.session.add(new_resume)
    # for i in words:
    #     print(new_resume.id)
    #     new_word = Text(words[i], words[i]['count'], words[i]['isHead'], words[i]['head'],new_resume)
    #     db.session.add(new_word)
    db.session.commit()
    return("Success")

@app.route('/<fname>/delete')
def delete_account(fname):
    the_user = db.session.query(User).filter_by(username=session.get('user')).one_or_none()
    db.session.delete(the_user)
    session.clear()
    db.session.commit()
    return redirect(url_for('home_page'))

app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)

# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000
