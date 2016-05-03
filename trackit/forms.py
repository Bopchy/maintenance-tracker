from flask.ext.wtf import Form
from wtfforms import StringField, BooleanField 
from wtfforms.validators import DataRequired  

class LoginForm(form): # instantiates form object 
	openid = StringField('openid', validators=[DataRequired()]) # DataRequired checks that the field is not submitted empty
	# Remember me option so user doesn't have to keep logging in each time
	remember_me = BooleanField('remember_me', default=False) 

