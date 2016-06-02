from flask import Blueprint 

main = Blueprint('main', __name__)
# Creating Blueprint by instantiating object of class Blueprint  
# The constructor for this class takes two required arguments: the 
# blueprint name (main) and the module or package where the blueprint is 
# located (like most flask apps, __name__ is appropriate here)

from . import views
# Importing views causes the routes to be associated with the blueprint
# Imported at the bottom to avoid circular imports issue