from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Required, Email

# Form on Sign In page 
class SignIn(Form):
	BizEmail = StringField('Business/Organization Email',\
		validators=[Required(), Email()])
	Password = PasswordField('Password', validators=[Required()])
	Remember_me = BooleanField('Keep me logged in')
	Submit = SubmitField('Sign In')
