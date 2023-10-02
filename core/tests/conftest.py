from os import environ
import pytest

from core.api import API

@pytest.fixture
def api():
    return API()

@pytest.fixture
def client(api):
    
    return api.test_client()


# TODO: Add more fixtures as needed