from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, PasswordField
from wtforms.validators import DataRequired, Optional
class Loginform(FlaskForm):

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    username = StringField('username'  )
    password = PasswordField('password' )
    email = StringField('email', )
    surname = StringField('surname' )
    name = StringField('name' )
    MiddleName= StringField('middleName')
    birthPlace = StringField('birthPlace')
    passport = StringField('passport')

