from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy  

trackit = Flask(__name__) # Application object created  
trackit.config.from_object('config') # Tells Flask to read and use config file  
db = SQLAlchemy(trackit) # Initializing database  

# Importing handlers from trackit package 
# Doing it in this position avoids circular import 
from trackit import handlers, models    
