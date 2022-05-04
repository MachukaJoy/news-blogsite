from flask import Flask
from config import config_options

from datetime import datetime

def format_datetime(value, format="%d-%m-%Y"):
    if value is None:
        return ""
    return datetime.strptime(value,"%Y-%m-%d").strftime(format)

#configured Jinja2 environment with user defined


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

     #register blueprint
    from .main import main as main_blueprint 
    app.register_blueprint(main_blueprint)
    app.jinja_env.filters['date_format']=format_datetime

    from .requests import configure_request
    configure_request(app)

    return app 