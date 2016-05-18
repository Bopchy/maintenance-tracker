from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField 
from wtforms.validators import Required, Email  

class LoginForm(Form): # instantiates form object 
	email = StringField('Email', validators=[Required(), Length(1, 64),
		Email()])
	password = PasswordField('Password', validators=[Required()])
	# PasswordField is an input element for the password 
	remember_me = BooleanField('Keep me logged in')
	# BooleanField is a checkbox
	submit = SubmitField('Log In')

