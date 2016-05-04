from trackit import trackit
from trackit import db
from trackit.models import Admin, StaffMemberProfile
from flask.ext.script import Manager, Shell

trackit.debug = True 
# Ensures server restarts itself when changes are made  
trackit.run() # Starts up the server with trackit application 

def make_shell_context():
	return dict(app=trackit, db=db, StaffMemberProfile=StaffMemberProfile)
manager.add_command("shell", Shell(make_context=make_shell_context)) 

if __name__ == '__main__':
	manager.run()