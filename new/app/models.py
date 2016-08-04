from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash 
from flask.ext.login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	 return User.query.get(int(user_id))
# This returns the user object if available, None otherwise  

class BizEmail(db.Model):
	__tablename__ = 'biz_emails'
	# It is convention to have table names be plurals 
	id = db.Column(db.Integer, primary_key=True)
	BizEmail = db.Column(db.String(100), unique=True, index=True)

########### Fix this table - BizEmail column  
class User(UserMixin, db.Model):
	__tablename__ = 'users' 
	# Defines name of the table in the database
	id = db.Column(db.Integer, primary_key=True) 
	BizEmail = db.Column(db.String(100), unique=True, index=True)
	BizName = db.Column(db.String(180), index=True)
	Password_hash = db.Column(db.String(128))
	role_id = db.Column(db.Integer,db.ForeignKey('roles.id')) 


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

class Role(db.Model):
	__tablename__='roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, unique=True, index=True, nullable=False)
	users = db.relationship('User', backref='role')
	# 1st argument of db.relationship() is the model on the other side of 
	# relationship, and 2nd, the reverse direction of the relationship 