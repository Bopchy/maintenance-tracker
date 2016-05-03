from flask import Flask 
 
trackit = Flask(__name__) # Application object created  
# Importing handlers from trackit package 
# Doing it in this position avoids circular import 
from trackit import handlers   
