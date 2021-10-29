from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    # app.config.from_object("app.config.setting")
    # app.config.from_object("app.config.secure")
    CORS(app, supports_credentials=True)

    return app
