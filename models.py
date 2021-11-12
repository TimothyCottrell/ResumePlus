from database import db
from sqlalchemy.dialects.sqlite import BLOB


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column("email", db.String(100))
    username = db.Column("username", db.String(100))
    fname = db.Column("fname", db.String(20))
    lname = db.Column("lname", db.String(20))
    password = db.Column("password", db.String(30))
    pfp = db.Column("pfp", db.LargeBinary())
    recruiter = db.Column("recruiter", db.Boolean)
    about = db.Column("about", db.String(500))
    phoneNumber = db.Column("phoneNumber", db.Integer)
    address = db.Column("address", db.String(50))
    city = db.Column("city", db.String(20))
    state = db.Column("state", db.String(2))
    zip = db.Column("zip", db.Integer)
    country = db.Column("country", db.String(20))

    resume = db.relationship("Resume", backref="User")

    def __init__(self, fname, lname, username, email, pwd, is_recruiter):
        self.email = email
        self.username = username
        self.fname = fname
        self.lname = lname
        self.password = pwd
        #self.pfp = pfp
        self.recruiter = is_recruiter

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.fname}', '{self.lname}','{self.password}', '{self.pfp}')"

    def change_about(self, about_me):
        self.about = about_me

    def change_location(self, address, city, state, zip, country):
        if not address == '':
            self.address = address
        if not city == '':
            self.city = city
        if not state == '':
            self.state = state
        if not zip == '':
            self.zip = int(zip)
        if not country == '':
            self.country = country

    def change_general_information(self, fname, lname, email, phoneNumber):
        if not fname == '':
            self.fname = fname
        if not lname == '':
            self.lname = lname
        if not email == '':
            self.email = email
        if not phoneNumber == '':
            self.phoneNumber = phoneNumber

    def change_password(self, new_password):
        if not new_password == '':
            self.password = new_password


# Just a start still gotta lot of planning to do
class Resume(db.Model):
    __tablename__ = 'Resume'
    id = db.Column("id", db.Integer, primary_key=True)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey('User.id'))
    html = db.Column('html', BLOB)
    category = db.Column("category", db.String(50))
    text = db.relationship("Text", backref="Resume")
    section = db.relationship("Section", backref="Resume")

    def __init__(self, user_id, html_in, cat):
        self.user_id = user_id
        self.html = html_in
        self.category = cat

    def __repr__(self):
        return f"Resume('{self.id}', '{self.category}', '{self.texts}')"


class Text(db.Model):
    __tablename__ = 'Text'
    id = db.Column("id", db.Integer, primary_key=True)
    word = db.Column("word", db.String(50))
    count = db.Column("count", db.Integer)
    isHead = db.Column("ishead", db.Boolean)
    head = db.Column("head", db.String(50))
    resume_id = db.Column("resume_id", db.Integer, db.ForeignKey('Resume.id'))

    def __init__(self, word, count, isHead, head, resume_id):
        self.word = word
        self.count = count
        self.isHead = isHead
        self.head = head
        self.resume_id = resume_id

    def __repr__(self):
        return f"Text('{self.word}', '{self.count}', '{self.isHead}', '{self.head}')"

class Section(db.Model):
    __tablename__ = 'Section'
    id = db.Column("id", db.Integer, primary_key=True)
    resume_id = db.Column("resume_id", db.Integer, db.ForeignKey('Resume.id'))
    name = db.Column("sectionName", db.String(20))
    info = db.Column("text", db.String(500))
    caption = db.Column("caption", db.String(500))

    def __init__(self, name, resume_id, info, caption):
        self.name = name
        self.info = info
        self.resume_id = resume_id
        self.caption = caption

    def __repr__(self):
        return f"Text('{self.name}', '{self.caption}', '{self.resume_id}', '{self.info}')"
