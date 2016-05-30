from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask.ext.script import Shell
from forms import SignUpForm, HomeSignUp, SignIn, RequestPost
from flask.ext.sqlalchemy import SQLAlchemy
import os 
import forms 

basedir = os.path.abspath(os.path.dirname(__file__))

# App Initialization-- trackit is object of Flask class
trackit = Flask(__name__)
# __name__ is used to determine the root path of the application 
# so it can find resource files relative to the location of the app
trackit.config['SECRET_KEY'] = 'amwjenfbtvpz' 
# Setting encryption key for CSRF
trackit.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
		os.path.join(basedir, 'trackit_data.sqlite')
# Creates database 'trackit_data.sqlite'
trackit.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
trackit.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(trackit) 
# This object instantiation of SQLAlchemy (db) represents the
# database and is what gives access to all functionality of 
# Flask-SQLAlchemy   
Bootstrap(trackit)

# Adding a shell context 
# 'make_shell_context' function registers the application, db instance, 
# models; so that they are automatically imported into the shell 
def make_shell_context():
	return dict(trackit=trackit, db=db, User=User, Requests=Requests)
manager.add_command("Shell", Shell(make_context=make_shell_context))

class User(db.Model):
	__tablename__ = 'user' 
	# Defines name of the table in the database
	id = db.Column(db.Integer, primary_key=True) 
	BizEmail = db.Column(db.String(100), unique=True, index=True)
	BizName = db.Column(db.String(180), index=True)
	Password = db.Column(db.String(15), nullable=False)

class Requests(db.Model):
	__tablename__='requests'
	id = db.Column(db.Integer, primary_key=True)
	Title = db.Column(db.String(120), nullable=False, index=True)
	Comments = db.Column(db.String(1800), nullable=False)

# View functions 
@trackit.route('/', methods=['GET', 'POST'])
@trackit.route('/home', methods=['GET', 'POST'])
def index():
# Variable BizEmail is to hold the value placed in BizEmail field
# on the form, when it becomes available 
# When value is unknown, BizEmail is equal to None
	BizEmail = None
	Form = HomeSignUp() 
# Handler created instance of the form class HomeSignUp  
	if Form.validate_on_submit():
# Validate_on_submit() returns True if form has been submitted, and 
# all validators were satisfied; otherwise it returns False   
		BizEmail = User.query.filter_by(BizEmail=Form.BizEmail.data)
		# Checks to see if submitted business email already exixts in db 
		if BizEmail is None:
			BizEmail = Form.BizEmail.data
			db.session.add(BizEmail) # Adds submitted email into db
			session['exists'] = False
			# 'exists' is a variable created to deal with the redirecting to a 
			# page stating that email already exists in the database. 
		else:
			session['exists'] = True
			#### Flash message stating email already exists in db
		session['BizEmail'] = Form.BizEmail.data
		Form.BizEmail.data = ''
		return redirect(url_for('index'))
	return render_template('home.html', Form=Form, \
		BizEmail=session.get('BizEmail')

@trackit.route('/signup', methods=['GET', 'POST'])
def register():
# Work on making this appear automatically, from when user
# put it in, in the Home page
	BizEmail = None
	BizName = None
	Password = None
	ConfirmPassword = None
	Form = SignUpForm()
	if Form.validate_on_submit():
		BizEmail = Form.BizEmail.data
		BizName = Form.BizName.data
		Password = Form.Password.data
		ConfirmPassword = Form.ConfirmPassword.data 
	return render_template('signup.html', Form=Form, BizEmail=BizEmail,\
		BizName=BizName, Password=Password, ConfirmPassword=ConfirmPassword)

@trackit.route('/signin', methods=['GET', 'POST'])
def signin():
	BizEmail = None
	Password = None
	Form = SignIn()
	if Form.validate_on_submit():
		BizEmail = Form.BizEmail.data
		Password = Form.Password.data
	return render_template('signin.html', Form=Form, BizEmail=BizEmail, \
		Password=Password)

@trackit.route('/postrequest', methods=['GET', 'POST'])
def postrequest():
	Title = None
	Comment = None
	Form = RequestPost()
	if Form.validate_on_submit():
		Title = Form.Title.data
		Comment = Form.Comment.data
	return render_template('postrequest.html', Form=Form, Title=Title, \
		Comment=Comment)

if __name__ == '__main__': 
# Ensures the development web server is started only when the script is executed 
# directly 
	trackit.debug=True # Activates debbuger and reloader
	trackit.run(host='0.0.0.0')