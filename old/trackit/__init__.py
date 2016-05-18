from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from .auth import auth as auth_blueprint 
#from main import main as main_blueprint
from config import config  

login_manager = LoginManager()
login_manager.session_protection = 'strong'
# Provides a 'strong' level of security against user session tampering
# - It will logout user if it detects change in user IP addrss or browser agent 
login_manager.login_view = 'auth.login'
# Is prefixed with 'auth' because login route is inside blueprint   

def create_app():
	trackit = Flask(__name__) # Application object created  
	db = SQLAlchemy(trackit) # Initializing database
	trackit.config.from_object(config['default']) 
	# Tells Flask to read and use config file
	login_manager.init_app(trackit)
	app.register_blueprint (auth_blueprint, url_prefix='/auth')

	return trackit
	 

# Importing handlers from trackit package 
# Doing it in this position avoids circular import 
from trackit import views, models    

