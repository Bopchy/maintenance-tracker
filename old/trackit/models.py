# Where all the database tables are defined 

from trackit import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask.ext.login import UserMixin 

# **** AUTHENTICATION ****
class User(UserMixin, db.Model):
	__tablename__= 'User'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(70), unique=True, index=True)
	username = db.Column(db.String(70), unique=True, index=True)
	password_hash = db.Column(db.String(120)) # Stores Password
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	def password(self):
		raise AttributeError('Password cannot be read')
		# Ensures password is write-only

	def password(self, password): 
		self.password_hash = generate_password_hash(password)
		# Hashes password 

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)
		# Verifies input password against hashed version to ensure 
		# its correct by passing it through the check_password_hash()

	def load_user(user_id):
		return User.query.get(int(user_id))
		# Receives user identifier as a Unicode string.Return valiue of 
		# the function must be the user object if available, otherwise 
		# None

