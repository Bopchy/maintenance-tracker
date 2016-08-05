from flask import render_template, session, url_for, flash, redirect
from flask.ext.login import login_user
from . import auth
from .forms import SignIn
from ..models import User

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
	Form = SignIn()
	if Form.validate_on_submit():
		user = User.query.filter_by(BizEmail=Form.BizEmail.data).first()
		# If the form data submitted is valid, the db is queried to see
		# if such an email as entered exists. 
		if user is not None and user.verify_password(Form.Password.data):
			login_user(user, Form.Remember_me.data) 
			# Records user as logged in, in a session
			return redirect(url_for('main.user_account'))
		# If the email exists, password is checked to see if it matches the one in the db. 
		# If it does, the user is logged in and proceeds to url_for(main.user_account). 
		flash('Invalid Business/Organization Email or Password.')
		# Else, the message above is flashed.
	return render_template('auth/signin.html', Form=Form)
	# Template stored inside templates/auth so as to avoid possible name collisions
	# with main-blueprint related templates  that may be added in the future