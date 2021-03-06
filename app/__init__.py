from flask import Flask
from flask_bootstrap import Bootstrap

from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

    # initializing application
    app = Flask(__name__)

    #creating the app config_options
    app.config.from_object(config_options[config_name])

    # initializing flask extensions
    bootstrap.init_app(app)

    # Reqistering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Setting config
    from .requests import configure_request
    configure_request(app)

    return app
