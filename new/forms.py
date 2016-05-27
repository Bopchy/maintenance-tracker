from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, TextAreaField 
from wtforms.validators import Required, Email, EqualTo, Length 

#def length_check(form, field): 
#	if len(field.data) > 100:
#		raise ValidationError('Field must be less than \
#			100 characters')

#def is_required(form, field):

# Form on Sign Up page 
class SignUpForm(Form):
	BizEmail = StringField('Business/Organization Email',\
		validators=[Required(), Email()])
	BizName = StringField('What is the name of your \
		Business/ Organization?',validators=[Required(), \
		Length(min=1, max=170)]) 
	Password = PasswordField('Password', validators=[Required()])
	ConfirmPassword = PasswordField('Re-type Password', \
		validators=[Required(), EqualTo(Password)])
	Submit = SubmitField('Sign Up')
	#PicUpload(Form):

# Form on Home page (for email) 
class HomeSignUp(Form):
	BizEmail = StringField('Business/ Organization Email',\
		validators=[Required(), Email()])
	Submit = SubmitField('Register as a new User')

# Form on Sign In page 
class SignIn(Form):
	BizEmail = StringField('Business/Organization Email',\
		validators=[Required(), Email()])
	Password = PasswordField('Password', validators=[Required()])
	Submit = SubmitField('Sign In')

# Form on Request page 
class RequestPost(Form):
	Title = StringField('Give your request a title', \
		validators=[Required()])
	Comment = TextAreaField('Tell us more about your request...',\
		validators=[Required(), Length(min=1, max=1800)])
	# upload photo
	Submit = SubmitField('Post Request')