import os
from flask import Flask

SECRET_KEY = os.getenv("FLASK_SECRET_KEY")


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY=SECRET_KEY)

    @app.route('/')
    def handle_root():
        return 'Well hello traveler'

    return app
