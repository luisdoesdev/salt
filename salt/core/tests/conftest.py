from os import environ
import pytest

from salt.salt import SALT as Salt

@pytest.fixture
def api():
    return Salt()

@pytest.fixture
def client(api,  method='GET', path='/'):
    environ = {
            'REQUEST_METHOD': method,
            'PATH_INFO': path,
            'wsgi.url_scheme': 'http',
            'wsgi.input': b""
        }
    return api.test_client(environ)


# TODO: Add more fixtures as needed