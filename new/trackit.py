from flask import Flask, render_template
 

# App Initialization-- trackit is object of Flask class
trackit = Flask(__name__)
# __name__ is used to determine the root path of the 
# application so it can find resource files relative
# to the location of the app

# View functions 
@trackit.route('/')
@trackit.route('/home')
def index():
	return render_template('home.html')

@trackit.route('/register')
def register():
	return render_template('register.html')


if __name__ == '__main__': # Ensures the development 
# web server is started only when the script is executed 
# directly 
	trackit.debug=True # Activates debbuger and reloader
	trackit.run(host='0.0.0.0')