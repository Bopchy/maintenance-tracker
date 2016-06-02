from . import db

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
	Password = db.Column(db.String(15), nullable=False)

class Requests(db.Model):
	__tablename__='requests'
	id = db.Column(db.Integer, primary_key=True)
	Title = db.Column(db.String(120), nullable=False, index=True)
	Comments = db.Column(db.String(1800), nullable=False)