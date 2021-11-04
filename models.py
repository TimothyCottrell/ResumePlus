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
    resumes = db.relationship("Resume", back_populates="user")

    def __init__(self, fname, lname, username, email, pwd):
        self.email = email
        self.username = username
        self.fname = fname
        self.lname = lname
        self.password = pwd

    def __repr__(self):
        return f"User('{self.id}', '{self.email}', '{self.username}', '{self.fname}', '{self.lname}','{self.password}')"


#Just a start still gotta lot of planning to do
class Resume(db.Model):
    __tablename__ = 'resume'
    id = db.Column("id", db.Integer, primary_key=True)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="resumes")
    html = db.Column('html', BLOB)
    category = db.Column("category", db.String(50))
    text = db.Column('text', db.String(300))
    headers = db.Column("headers", db.String(300))

    def __init__(self, user_id, html_in, cat, text_in, headers_in):
        self.user_id = user_id
        self.html = html_in
        self.category = cat
        self.text = text_in
        self.headers = headers_in

    def __repr__(self):
        return f"Resume('{self.id}', '{self.category}', '{self.text}', '{self.headers}')"