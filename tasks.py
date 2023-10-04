#!/usr/bin/env python3
from invoke.tasks import task 
import logging

'''
    pip3 install virtualenv - to install virtualenv
    virtualenv -p python3 salt - to create virtual environment
    source salt/bin/activate - to activate virtual environment

    pip install invoke
    invoke install - to install dependencies
    
    soure venv/bin/activate - to activate virtual environment
    invoke test    - to run tests
    invoke app     - to run the app
'''

@task
def install(c):
    c.run("pip3 install -r core/requirements.txt")

@task
def tests(c):
    try:
        c.run("PYTHONPATH=. pytest --cov=.")
    except Exception as e:
        logging.error(f"An error occurred: Try running 'invoke install' to install dependencies")

@task
def app(c):
    try:
        c.run("gunicorn --chdir core app:app")

    except Exception as e:
        logging.error(f"An error occurred: Try running 'invoke install' to install dependencies")
