import os
from flask import Flask
from .db import engine, Base, Type, Session

Base.metadata.create_all(engine)
session = Session()
type_example = Type(name='Car', props_ids=[1, 2])
session.add(type_example)
session.commit()


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY=os.getenv('FLASK_SECRET_KEY'))

    @app.route('/')
    def handle_root():
        return 'Well hello traveler'

    return app
