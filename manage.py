from app import app
from flask_script import Manager,Server

#import creat_app function from __init__.py
from app import create_app

#create an instance of app
app= create_app('development')
manager=Manager(app)
manager.add_command('server',Server)



if __name__=='__main__':
    manager.run()