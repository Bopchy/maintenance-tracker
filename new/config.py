import os 

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY = 'amwjenfbtvpz' # Setting encryption key for CSRF
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	### DEVELOPMENT DATABASE ###
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
		os.path.join(basedir, 'trackit_data.sqlite')
	# Creates database 'trackit_data.sqlite'
	DEBUG = None

	@staticmethod
	def init_app(trackit):
		pass


config ={
	'default' : Config
	}

 
