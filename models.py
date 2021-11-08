from database import db
from sqlalchemy.dialects.sqlite import BLOB

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column("email", db.String(100))
    username = db.Column("username", db.String(100))
    fname = db.Column("fname", db.String(20))
    lname = db.Column("lname", db.String(20))
    password = db.Column("password", db.String(30))
    recruiter = db.Column("recruiter", db.Boolean)
    resume = db.relationship("Resume", back_populates="user")

    def __init__(self, fname, lname, username, email, pwd, is_recruiter):
        self.email = email
        self.username = username
        self.fname = fname
        self.lname = lname
        self.password = pwd
        self.recruiter = is_recruiter

    def __repr__(self):
        return f"User('{self.id}', '{self.email}', '{self.username}', '{self.fname}', '{self.lname}','{self.password}')"


#Just a start still gotta lot of planning to do
class Resume(db.Model):
    __tablename__ = 'resume'
    id = db.Column("id", db.Integer, primary_key=True)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="resume")
    html = db.Column('html', BLOB)
    category = db.Column("category", db.String(50))
    text = db.relationship("Text", back_populates="resume")

    def __init__(self, user_id, html_in, cat):
        self.user_id = user_id
        self.html = html_in
        self.category = cat

    def __repr__(self):
        return f"Resume('{self.id}', '{self.category}', '{self.text}')"

class Text(db.Model):
    __tablename__ = "text"
    id = db.Column("id", db.Integer, primary_key=True)
    word = db.Column("word", db.String(50))
    count = db.Column("count", db.Integer)
    isHead = db.Column("ishead", db.Boolean)
    head = db.Column("head", db.String(50))
    resume_id = db.Column("res_id", db.Integer, db.ForeignKey('resume.id'))
    resume = db.relationship("Resume", back_populates="text")



    def __init__(self,word,count,isHead,head,r):
        self.word = word
        self.count = count
        self.isHead = isHead
        self.head = head
        self.resume = r

    def __repr__(self):
        return f"Text('{self.word}', '{self.count}', '{self.isHead}', '{self.head}')"
