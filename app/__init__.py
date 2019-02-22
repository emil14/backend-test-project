import os
from flask import Flask
from . import db

type = db.Type(name='Car', props_ids=[1, 2])


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY=os.getenv('FLASK_SECRET_KEY'))

    @app.route('/')
    def handle_root():
        return 'Well hello traveler'

    return app
