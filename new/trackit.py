from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import forms
from forms import SignUpForm, HomeSignUp, SignIn, RequestPost
 

# App Initialization-- trackit is object of Flask class
trackit = Flask(__name__)
# __name__ is used to determine the root path of the application 
# so it can find resource files relative to the location of the app
trackit.config['SECRET_KEY'] = 'amwjenfbtvpz' 
# Setting encryption key for CSRF
Bootstrap(trackit)

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
		BizEmail = Form.BizEmail.data
		Form.BizEmail.data = ''
	return render_template('home.html', Form=Form, \
		BizEmail=BizEmail)

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


if __name__ == '__main__': # Ensures the development 
# web server is started only when the script is executed 
# directly 
	trackit.debug=True # Activates debbuger and reloader
	trackit.run(host='0.0.0.0')