# Is the views module which deals with handlers 
# Imports the Flask instance trackit from trackit package 
from flask import render_template, flash, redirect, request, url_for
from flask.ext.login import login_user
from trackit import trackit
from forms import LoginForm
from . import auth

@trackit.route('/')
@trackit.route('/index')
def index():
	user = {'nickname':'Bopchy'}
	return render_template('index.html', title='Home', user=user)

@auth.route('/login') #methods=['GET', 'POST'])
def login():
	# Imports and instantiates an object of LoginForm class, form = object
	# form = LoginForm() 
	# if form.validate_on_submit(): # That is, if an empty form is submitted
	# 	flash('Login requires that you input your User_ID="%s", remember_me=%s'
	# 		%(form.openid.data, str(form.remember_me.data)))
	# 	return redirect ('/index') 
	return render_template('auth/login.html')


	
