import os
from flask import Flask
from flask_cors import CORS
from waitress import serve
from dotenv import load_dotenv

load_dotenv()


def create_app(config={}):
    app = Flask(__name__)
    # app.config.from_object("app.config.setting")
    # app.config.from_object("app.config.secure")
    CORS(app, supports_credentials=True)
    app.config.update(config)

    return app


if __name__ == "__main__":
    app = create_app()
    HOST = os.getenv("FLASK_RUN_HOST", default="127.0.0.1")
    PORT = os.getenv("FLASK_RUN_PORT", default=5000)
    DEBUG = os.getenv("FLASK_DEBUG", default=False)

    if DEBUG:
        app.run(
            host=HOST,
            port=PORT,
            debug=DEBUG,
        )
    else:
        serve(app, host=HOST, port=PORT)
