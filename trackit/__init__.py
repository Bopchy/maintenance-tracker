from flask import Flask 
 
trackit = Flask(__name__) # Application object created  
trackit.config.from_object('config')

# Importing handlers from trackit package 
# Doing it in this position avoids circular import 
from trackit import handlers   
