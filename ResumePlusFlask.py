import os  # os is used to get environment variables IP & PORT
from flask import Flask  # Flask is the web app that we will customize
from flask import render_template
from flask import request, Response
from flask import jsonify
from flask import redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import nltk
from nltk.corpus import stopwords
import bitstring
import json
from database import db
from models import User, Resume, Text, Section
import bcrypt
import pickle

app = Flask(__name__)  # create an app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resumeplus_flask_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'SE3155'
nltk.download('stopwords')
stop = stopwords.words('english')
bcryptCode = 'utf-8'

db.init_app(app)
with app.app_context():
    db.create_all()  # run under the app context

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
        the_user = db.session.query(User).filter_by(username=session.get('user')).one_or_none()
        the_resume = db.session.query(Resume).filter_by(user_id=the_user.id).one_or_none()
        sections = db.session.query(Section).filter_by(resume_id=the_resume.id).all()
        return render_template('Home.html', user=the_user, resume=the_resume, sections=sections)
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

@app.route('/database')
def database():
    if session.get('user'):
        return render_template('Database.html', user=session['user'])
    return render_template('Database.html')

@app.route('/save_resume', methods=['POST'])
def save_resume():
    data = json.loads(request.get_data())
    html = ''
    words = {}
    curHead = None
    for i in data:
        ## Parse the text and loop through
        split = data[i]['text'].split()
        if len(split) > 0:
            for x in split:
                count = 0
                isHead = False
                head = curHead
                ## If its not a stop word like is and a
                if not x in stop:
                    # If we already have it count it again
                    if x in words:
                        count = words[x]['count'] + 1
                    else:  # If we have not seen this word yet
                        count = 1
                        ht = data[i]['html']
                    if ht[1] == "h":  # if its a header
                        isHead = True
                        curHead = x
                    words[x] = {  ## assign it to words
                        "count": count,
                        "isHead": isHead,
                        "head": head
                    }
        html += data[i]['html']
    bhtml = html.encode(bcryptCode)
    the_user = db.session.query(User).filter_by(username=session.get('user')).one_or_none()
    new_resume = Resume(the_user.id, bhtml, "testing")
    db.session.add(new_resume)
    for i in words:
        new_word = Text(i, words[i]['count'], words[i]['isHead'], words[i]['head'], new_resume.id)
        db.session.add(new_word)
    db.session.commit()
    return "Success"

# @app.route('/get_html', methods=['POST', 'GET'])
# def get_html():
#    data = {'0': {'html': '<h1>Amazing Header</h1>', 'text': 'Amazing Header'},
#            '1': {'html': '<p>This text is different!</p>',
#                  'text': 'This text is different!'}}
#    return None

@app.route('/account/change_location', methods=['POST'])
def change_location():
    if request.method == 'POST':
        the_user = db.session.query(User).filter_by(username=session.get('user')).one_or_none()
        the_user.change_location(request.form['address'], request.form['city'], request.form['state'],
                                 request.form['zip'], request.form['country'])
        db.session.add(the_user)
        db.session.commit()
    return redirect(url_for('settings'))

@app.route('/account/change_general_information', methods=['POST'])
def change_general_information():
    if request.method == 'POST':
        the_user = db.session.query(User).filter_by(username=session.get('user')).one_or_none()
        the_user.change_general_information(request.form['fname'], request.form['lname'], request.form['email'],
                                            request.form['phoneNumber'])
        db.session.add(the_user)
        db.session.commit()
    return redirect(url_for('settings'))

@app.route('/account/change_about', methods=['POST'])
def change_about():
    if request.method == 'POST':
        the_user = db.session.query(User).filter_by(username=session.get('user')).one_or_none()
        the_user.change_about(request.form['about'])
        db.session.add(the_user)
        db.session.commit()
    return redirect(url_for('settings'))

@app.route('/account/add_section/<section_name>', methods=['POST'])
def add_section(section_name):
    if request.method == 'POST':
        the_user = db.session.query(User).filter_by(username=session.get('user')).one_or_none()
        the_resume = db.session.query(Resume).filter_by(user_id=the_user.id).one_or_none()
        info, caption = '', ''
        for keyvalue in request.form.lists():
            if not (value for value in keyvalue[1]) == '':
                for value in keyvalue[1]:
                    if not value == '':
                        if section_name == 'skills':
                            skills = value.split(",")
                            for i, skill in enumerate(skills):
                                info += skill + "\n"
                                caption += "skill " + str(i + 1) + "\n"
                        else:
                            info += value + "\n"
                            caption += keyvalue[0] + "\n"
        new_section = Section(the_resume.id, section_name, info, caption)
        db.session.add(new_section)
        db.session.commit()
    return redirect(url_for('settings'))

@app.route('/account/change_password', methods=['POST'])
def change_password():
    if request.method == 'POST':
        the_user = db.session.query(User).filter_by(username=session.get('user')).one_or_none()
        if request.form['current-password'] == request.form['confirm-password'] and bcrypt.checkpw(
                request.form['current-password'].encode(bcryptCode), the_user.password):
            the_user.change_password(bcrypt.hashpw(request.form['new-password'].encode(bcryptCode), bcrypt.gensalt()))
            db.session.add(the_user)
            db.session.commit()
    return redirect(url_for('settings'))

@app.route('/<fname>/delete')
def delete_account(fname):
    the_user = db.session.query(User).filter_by(username=session.get('user')).one_or_none()
    db.session.delete(the_user)
    session.clear()
    db.session.commit()
    return redirect(url_for('home_page'))

@app.route('/clear')
def clear():
    session.clear()
    db.session.commit()
    return redirect(url_for('home_page'))

app.run(host=os.getenv('IP', '127.0.0.1'), port=int(os.getenv('PORT', 5000)), debug=True)

# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000
