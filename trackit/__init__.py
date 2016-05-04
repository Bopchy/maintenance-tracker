from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand  
from main import main as main_blueprint
from config import config  

#def create_app():
trackit = Flask(__name__) # Application object created  

db = SQLAlchemy(trackit) # Initializing database
migrate = Migrate(trackit, db)  

manager = Manager(trackit)
manager.add_command ('db', MigrateCommand)

trackit.config.from_object(config['default']) 
	# Tells Flask to read and use config file  
	
	#app.register_blueprint(main_blueprint)

	#return app

# Importing handlers from trackit package 
# Doing it in this position avoids circular import 
from trackit import handlers, models    
