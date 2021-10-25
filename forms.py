from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TextAreaField, FileField, IntegerField
from wtforms.validators import Length, DataRequired, EqualTo, Email, NumberRange
from wtforms import ValidationError
from models import User
from database import db

class RegisterForm(FlaskForm):
    class Meta:
        csrf = False

    username = StringField('Username',
                        [Email(message='Not a valid email address.'), DataRequired()])

    fname = StringField("FirstName", DataRequired(message="Please enter your first name."))

    lname = StringField("LastName", DataRequired(message="Please enter your last name."))

    password = PasswordField('Password',
                             [DataRequired(message="Please enter a password."),
                              EqualTo('confirmPassword', message='Passwords must match')])

    confirmPassword = PasswordField('Confirm Password',
                                    validators=[Length(min=1, max=10)])

    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    class Meta:
        csrf = False

    username = StringField('Username', validators=[Length(1, 100)])

    password = PasswordField('Password', [
        DataRequired(message='Please enter a password.')])

    submit = SubmitField('Submit')
