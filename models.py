from database import db

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    username = db.Column("username", db.String(100))
    fname = db.Column("fname", db.String(20))
    lname = db.Column("lname", db.String(20))
    password = db.Column("password", db.String(30))

    def __init__(self, fname, lname, email, pwd):
        self.username = email
        self.fname = fname
        self.lname = lname
        self.password = pwd

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.fname}', '{self.lname}','{self.password}')"

#Just a start still gotta lot of planning to do
# class Resume(db.Model):
#     id = db.Column("id", db.Integer, primary_key=True)
    
