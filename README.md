# Prerequisites

You need to install [PostgreSQL](https://www.postgresql.org/download/) and [Python](https://docs.python-guide.org/starting/install3/). Here's how you can do it on Ubuntu Linux:

```shell
sudo apt update
sudo apt install python3.7 postgresql-10
```

Now now you need to install and run [pipenv](https://pipenv.readthedocs.io/en/stable/install/) to create virtualenv and manage our dependencies:

```shell
pip install pipenv
pipenv --three # create a virtualenv
pipenv install --dev # install dependencies
```

# Getting started

Make sure you have `.env` file setup. Then go to the terminal and type:

```shell
pipenv shell # enter the matrix
flask run # start web-server

# run PostgreSQL shell:
sudo su - postgres
psql
```
