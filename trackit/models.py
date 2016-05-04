# Where all the database tables are defined 

from trackit import db

class Admin(db.Model):
	__tablename__= 'Admin'
	id = db.Column(db.Integer, index=True, primary_key=True)
	#level = db.Column(db.Integer, index=True, level=2)

class StaffMemberProfile(db.Model):
	__tablename__= 'StaffMemberProfile'
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(80), index=True)
	last_name = db.Column(db.String(80), index=True)
	phone_no = db.Column(db.Integer, index=True, unique=True)
	email = db.Column(db.String(100), index=True, unique=True)
	requests = db.relationship('RequestsLog', backref='staff', lazy='dynamic')
	#level = db.Column(db.Integer, index=True, level=3)
	# Defines what will be returned when yo+u query table StaffMemberProfile
	def __repr__(self):
		return '<StaffMember (staff_id='%r', first_name='%r', last_name='%r',\
			email='%r', phone_no='%r')>' % (self.staffid, self.first_name, \
			self.last_name, self.email, self.phone_no)

class ClientProfile(db.Model):
	__tablename__= 'ClientProfile'
	id = db.Column(db.Integer, primary_key=True)
	client_name = db.Column(db.String, index=True)
	phone_no = db.Column(db.Integer, index=True, unique=True)
	email = db.Column(db.String, index=True, unique=True)
	requests = db.relationship('RequestsLog', backref='client', lazy='dynamic')
	#level = db.Column(db.Integer, index=True, level=3)
	
	def __repr__(self):
		return '<ClientProfile (client_name='%r', phone_no='%r', email='%r'\
			requests='%r')>' % (self.client_name, self.phone_no, self.email, \
			self.requests)

class RequestsLog(db.Model):
	__tablename__= 'RequestsLog'
	id = db.Column(db.Integer, primary_key=True, unique=True)
	request_summ = db.Column(db.String(200), index=True)
	body = db.Column(db.String(2000), index=True)
	timestamp = db.Column(db.DateTime)
	client_id = db.Column(db.Integer, db.ForeignKey('ClientProfile.id'))
	staff_id = db.Column(db.Integer, db.ForeignKey('StaffMemberProfile.id')) 
	# ForeignKeys contains id of user who posted request, through this it 
	# links users to the posts that they write enabling us to query 
	def __repr__(self):
		return '<RequestsLog (request_summ='%r', body='%r', timestamp='%r', \
			client_id='%r', staff_id='%r')>' % (self.request_summ, self.body, \
			self.timestamp, self.client_id, self.staff_id) 
	
