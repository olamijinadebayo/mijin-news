from flask_script import Server,Manager,Shell

from app import create_app

#Flask-Script is a command line parser for creating startup configurations.
# Manager initializes the flask script extension
# Server helps us launch the server
# Creating the app instance

# creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

@manager.command
def test():
    '''
    this will rin unittests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
