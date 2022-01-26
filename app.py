import os
from flask import Flask
from flask_cors import CORS


def create_app(config={}):
    app = Flask(__name__)
    # app.config.from_object("app.config.setting")
    # app.config.from_object("app.config.secure")
    CORS(app, supports_credentials=True)
    app.config = config
    return app


if __name__ == "__main__":
    app = create_app()
    HOST = os.getenv("FLASK_RUN_HOST", default="127.0.0.1")
    PORT = os.getenv("FLASK_RUN_PORT", default=5000)
    DEBUG = os.getenv("FLASK_DEBUG", default=False)

    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG,
    )
