#!/bin/sh
export FLASK_APP=./app/index.py
export FLASK_RUN_PORT=8080
source $(pipenv --venv)/bin/activate
flask run
