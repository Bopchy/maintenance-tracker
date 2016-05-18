from flask import Flask

# App Initialization-- trackit is object of Flask class
trackit = Flask(__name__)
# __name__ is used to determine the root path of the 
# application so it can find resource files relative
# to the location of the app

# View functions 
@trackit.route('/')
def index():
	return "<h1>Hello Bopchy!!</h1>"

@trackit.route('/browser')
def browser():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your browser is %s!' % user_agent

@trackit.route('/user/<name>')
def user(name):
	return '<h2>Hello, %s!</h2>' % name

if __name__ == '__main__': # Ensures the development 
# web server is started only when the script is executed 
# directly 
	trackit.debug==True # Activates debbuger and reloader
	trackit.run()