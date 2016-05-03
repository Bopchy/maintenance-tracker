from trackit import db

class AdminLogin(db.Model):
	pass

class StaffMemberProfile(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(80), index=True, unique=True)
	last_name = db.Column(db.String(80), index=True, unique=True)
	phone_no = db.Column(db.Integer, index=True, unique=True)
	email = db.Column(db.String(100), index=True, unique=True)

	def __repr__(self):
		return '<StaffMember (first_name='%r', last_name='%r', email='%r')>' % (self.first_name, self.last_name, self.email)

class ClientProfile(db.Model):
	pass

class RequestsLog(db.Model):
	# id ~~ primary key
	# body
	# timestamp
	# user_id ~~ foreign key # Links users to the posts that they write
	pass
