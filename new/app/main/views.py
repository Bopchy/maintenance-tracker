from flask import render_template, url_for, session, redirect, request
from .forms import SignUpForm, HomeSignUp, SignIn, RequestPost 
from ..models import BizEmail, User, Requests
from .. import db
from . import main

@main.route('/', methods=['GET', 'POST'])
@main.route('/home', methods=['GET', 'POST'])
def index():
# Variable BizEmail is to hold the value placed in BizEmail field
# on the form, when it becomes available 
# When value is unknown, BizEmail is equal to None
	biz_emails = None
	Form = HomeSignUp() 
	# Handler created instance of the form class HomeSignUp  
	if request.method == 'POST':
		# Checks to see if required form validators have been satisfied 
		# Checks to see if submitted business email already exists in db 
		if biz_emails is None:
			biz_emails = BizEmail(BizEmail=Form.BizEmail.data)
			Form.populate_obj(biz_emails)
			db.session.add(biz_emails) # Adds submitted email into db
			db.session.commit()
			session['exists'] = False
				# 'exists' is a variable created to deal with the redirecting to a 
				# page stating that email already exists in the database. 
		else:
			session['exists'] = True
			#### Flash message stating email already exists in db
		session['BizEmail'] = Form.BizEmail.data
		# Ensures value stored in BizEmail is remembered past the request
		Form.BizEmail.data = ''
		# Clears the form field by making it into an empty string 
		return redirect(url_for('.register'))
		# Its only forms with valid inputted data that can move on to the 
		# /signup.html page
	return render_template('home.html', Form=Form, \
		BizEmail=session.get('BizEmail'))
	# If BizEmail is None there will be no error because the get() automatically 
	# returns None when there is no value (see page 46 Flask Web Devlpmnt)

@main.route('/signup', methods=['GET', 'POST'])
def register():
	biz_emails = session.get('BizEmail')
	# Places email entered on the home page, in the email slot on sign up page
	biz_name = None
	password = None
	confirm_password = None
	Form = SignUpForm()
	if request.method =='POST' and Form.validate_on_submit():
		biz_name = User(BizName=Form.BizName.data)
		Form.populate_obj(biz_name)
		db.session.add(biz_name) 
		db.session.commit()
		password = User(Password=Form.Password.data)
		Form.populate_obj(password)
		db.session.add(password)
		db.session.commit()
		### Deal with password confirmation
		Form.BizEmail.data = '' 
		Form.BizName.data  = ''
		Form.Password.data = ''
		Form.ConfirmPassword.data = ''
		return redirect(url_for('.signin'))
	return render_template('signup.html', Form=Form, BizEmail=biz_emails,\
		BizName=biz_name, Password=password, ConfirmPassword=confirm_password)

@main.route('/signin', methods=['GET', 'POST'])
def signin():
	BizEmail = None
	if session['BizEmail']:
		BizEmail = BizEmail
	Password = None
	Form = SignIn()
	if Form.validate_on_submit():
		BizEmail = Form.BizEmail.data
		Password = Form.Password.data
	return render_template('signin.html', Form=Form, BizEmail=BizEmail, \
		Password=Password)

@main.route('/postrequest', methods=['GET', 'POST'])
def postrequest():
	Title = None
	Comment = None
	Form = RequestPost()
	if Form.validate_on_submit():
		Title = Form.Title.data
		Comment = Form.Comment.data
	return render_template('postrequest.html', Form=Form, Title=Title, \
		Comment=Comment)

@main.route('/user')
def user_account():
	return render_template('user.html')
