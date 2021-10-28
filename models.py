from database import db

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(100))
    fname = db.Column("fname", db.String(20))
    lname = db.Column("lname", db.String(20))
    password = db.Column("password", db.String(30))
    pfp = db.Column("pfp", db.LargeBinary())

    def __init__(self, fname, lname, email, pwd):
        self.username = email
        self.fname = fname
        self.lname = lname
        self.password = pwd
        #self.pfp = pfp

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.fname}', '{self.lname}','{self.password}', '{self.pfp}')"

#Just a start still gotta lot of planning to do
class Resume(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    user = db.Column("username", db.String(100))
    html = db.Column('html', db.String(300))
    category = db.Column("category", db.String(50))
    text = db.Column('text', db.String(300))
    headers = db.Column("text", db.String(300))



    def __init__(self, user_in, html_in, cat, text_in, headers_in):
        user = user_in
        html = html_in
        category = cat
        text = text_in
        headers = headers_in

    def __repr__(self):
        return f"Resume('{self.id}', '{self.html}', '{self.category}', '{self.text}', '{self.headers}')"
