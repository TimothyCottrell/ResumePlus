from database import db

class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    fname = db.Column("first_name", db.String(30))
    lname = db.Column("last_name", db.String(30))
    username = db.Column("username", db.String(100))
    password = db.Column("password", db.String(30))

    def __init__(self, fname, lname, email, pwd):
        self.username = email
        self.password = pwd
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"User('{self.id}',{self.fname}, {self.lname} ,'{self.username}, '{self.password}')"
