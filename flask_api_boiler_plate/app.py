from flask import Flask
from flask_cors import CORS


def create_app(config={}):
    app = Flask(__name__)
    # app.config.from_object("app.config.setting")
    # app.config.from_object("app.config.secure")
    CORS(app, supports_credentials=True)
    app.config = config
    return app
