from trackit import trackit, db
from trackit.models import User
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand 

trackit.debug = True 
# Ensures server restarts itself when changes are made  
trackit.run() # Starts up the server with trackit application 

migrate = Migrate(trackit, db)  
manager = Manager(trackit)


def make_shell_context():
	return dict(app=trackit, db=db, StaffMemberProfile=StaffMemberProfile)

manager.add_command("shell", Shell(make_context=make_shell_context)) 
manager.add_command ('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()