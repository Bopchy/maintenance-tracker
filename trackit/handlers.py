# Is the handlers module 
# Imports the Flask instance trackit from trackit package 
from flask import render_template, flash, redirect
from trackit import trackit
from forms import LoginForm

@trackit.route('/')
@trackit.route('/index')
def index():
	user = {'nickname':"Bopchy"}
	return render_template('index.html', title='hume', user=user)

@trackit.route('/login', methods=['GET', 'POST'])
def login():
	# Imports and instantiates an object of LoginForm class, form = object
	form = LoginForm() 
	return render_template('login.html', title='Sign In', form=form)


	
