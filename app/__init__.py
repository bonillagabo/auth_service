from flask import Flask
from .config import Config
from .routes.test import test_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    app.register_blueprint(test_routes, url_prefix="/api")

    return app
