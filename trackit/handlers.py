# Is the handlers module 
# Imports the Flask instance trackit from trackit package 
from flask import render_template
from trackit import trackit

@trackit.route('/')
@trackit.route('/index')
def index():
	user = {'nickname':"Bopchy"}
	return render_template('index.html', title='hume', user=user)


	
