from flask import Blueprint 

auth = Blueprint('auth', __name__) # Creates blueprint object
# Imports routes from handlers.py, thus defining the route associated with 
# authentication
from trackit import views