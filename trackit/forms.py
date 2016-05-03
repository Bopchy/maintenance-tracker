from flask.ext.wtf import Form
from wtforms import StringField, BooleanField 
from wtforms.validators import DataRequired  

class LoginForm(Form): # instantiates form object 
	openid = StringField('openid', validators=[DataRequired()]) # DataRequired checks that the field is not submitted empty
	# Remember me option so user doesn't have to keep logging in each time
	remember_me = BooleanField('remember_me', default=False) 

