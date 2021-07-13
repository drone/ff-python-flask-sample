import os
from flask import Flask
from flask_cors import CORS

from .error_handler import init_errorhandler


def create_app(test_config=None):

    from . import dashboard

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'app.sqlite'),
    )
    CORS(app, resources={r"/.*": {"origins": "*"}})
    app.config['CORS_HEADERS'] = 'Content-Type'

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    init_errorhandler(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(dashboard.bp)

    return app
