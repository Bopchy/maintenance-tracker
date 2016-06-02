import os
from app import create_app, db
from app.models import BizEmail, User, Requests
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand, Migrate

trackit = create_app(os.getenv ('FLASK_CONFIG') or 'default')
# Application created using the default configurations  
manager = Manager(trackit)
migrate = Migrate(trackit, db)
# Initialization of Flask-Script and Flask-Migrate respectively 

# Adding a shell context 
# def make_shell_context():
# 	return dict(trackit=trackit, db=db, BizEmail=BizEmail, User=User, \
# 		Requests=Requests)
# # 'make_shell_context' function registers the application, db instance, 
# # models; so that they are automatically imported into the shell 
# manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__': 
	#manager.run()
# Ensures the development web server is started only when the script is executed 
# directly 
	trackit.debug = True # Activates debbuger and reloader
	trackit.run(host='0.0.0.0')