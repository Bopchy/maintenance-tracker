import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Shows path to our database file 
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'trackit.db')
# Folder that will store all the SQLALchemy migrate data files 
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True 
# Tracks the modifications to objects and emits signals    

# Holds cofiguration information for Flask-WTF
WTF_CSRF_ENABLED = True # Activates CSRF prevention, making your app more secure 
SECRET_KEY = "secret_key" # Creates cryptogra[hic token used to validate form
# SECRET_KEY should be something difficult to guess
