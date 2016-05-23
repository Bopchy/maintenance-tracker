from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField 
from wtforms.validators import Required, Email, EqualTo 

def length_check(form, field): 
	if len(field.data) > 100:
		raise ValidationError('Field must be less than \
			100 characters')

#def is_required(form, field):

class RegisterForm(Form):
	BizEmail = StringField('Business/Organization Email',\
		validators=[Required(), Email()])
	BizName = StringField('What is the name of your \
		Business/ Organization?',validators=[Required(), \
		length_check()]) 
	Password = PasswordField('Password', validators=[Required()])
	ConfirmPassword = PasswordField('Retype Password', \
		validators=[Required(), EqualTo(Password)])
	Submit = SubmitField('Sign Up')

#class PicUpload(Form):