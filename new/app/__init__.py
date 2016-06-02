from flask import Flask, render_template, redirect, url_for, session, request
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from config import config 

# Creation of uninitialized flask extensions in use 
# (extensions imported above). They are uninitialized because there is 
# no application instance to initlaize them with  
bootstrap = Bootstrap()
db = SQLAlchemy()
# This object instantiation of SQLAlchemy (db) represents the
# database and is what gives access to all functionality of 
# Flask-SQLAlchemy

##### Factory function for trackit app #####
def create_app(config_name): 
	# This function takes as an argument the name of a configuration to 
	# use for the application 
	# App Initialization
	trackit = Flask(__name__)
	# __name__ is used to determine the root path of the application 
	# so it can find resource files relative to the location of the app
	trackit.config.from_object(config[config_name])
	config[config_name].init_app(trackit)

	bootstrap.init_app(trackit)
	db.init_app(trackit)

	# Registering the blueprint with the application
	from main import main as main_blueprint 
	trackit.register_blueprint(main_blueprint) 

	return trackit
	# Returns created application instance 

