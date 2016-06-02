from flask import render_template 
from . import main 

 @main.trackit_errorhandler(404):
 def page_not_found(e):
 	return render_template('404.html'), 404
 	# Specifies page to return for error code 404
 	# trackit_errorhandler used, as opposed to just error_handler 
 	# because the former captures errors that occur application-wide,
 	# while the latter only captures errors that originate in the 
 	# blueprint    

 @main.trackit_errorhandler(500):
 def internal_server_error(e):
 	return render_template('500.html'), 500