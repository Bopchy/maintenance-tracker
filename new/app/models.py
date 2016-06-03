from . import db
from werkzeug.security import generate_password_hash, check_password_hash 

class BizEmail(db.Model):
	__tablename__ = 'biz_emails'
	id = db.Column(db.Integer, primary_key=True)
	BizEmail = db.Column(db.String(100), unique=True, index=True)

########### Fix this table - BizEmail column  
class User(db.Model):
	__tablename__ = 'user' 
	# Defines name of the table in the database
	id = db.Column(db.Integer, primary_key=True) 
	BizEmail = db.Column(db.String(100), unique=True, index=True)
	BizName = db.Column(db.String(180), index=True)
	Password_hash = db.Column(db.String(128))

	@property 
	def password(self):
		raise AttributeError('Password is not a readbale attribute')
	# This property implements the password hashing function 
	# This ensures the original password cannot be read once hashed 

	@password.setter
	def password(self, password):
		self.Password_hash = generate_password_hash(password)
	# Calls the Werkzeug generate_password_hash() and writes the result
	# to the password hash field  

	def verify_password(self, password):
		return check_password_hash(self.Password_hash, password)
	# This takes a password and passes it to check_password_hash() for 
	# verification against the hashed verison stored in User model 

class Requests(db.Model):
	__tablename__='requests'
	id = db.Column(db.Integer, primary_key=True)
	Title = db.Column(db.String(120), nullable=False, index=True)
	Comments = db.Column(db.String(1800), nullable=False)