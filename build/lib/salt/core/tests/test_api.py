import pytest
from api import API

# Fixture for the API instance
@pytest.fixture
def api():
    return API('core/templates')

# Fixture for the test client
@pytest.fixture
def client(api):
    return api.test_client()

def test_route_addition_and_access(api, client):
    @api.route("/test")
    def test_route(req, resp):
        resp.text = "Test Route"

    response = client.get("http://testserver/test")
    assert response.status_code == 200
    assert response.text == "Test Route"

def test_non_existent_route(client):
    response = client.get("http://testserver/non_existent")
    assert response.status_code == 404
    assert response.text == "Not found"

def test_duplicate_route_assertion(api):
    @api.route("/duplicate")
    def duplicate_route(req, resp):
        resp.text = "Duplicate Route"

    with pytest.raises(AssertionError):
        @api.route("/duplicate")
        def another_duplicate_route(req, resp):
            resp.text = "Another Duplicate Route"

def test_route_with_named_parameters(api, client):
    @api.route("/greet/{name}")
    def greet_route(req, resp, name):
        resp.text = f"Hello, {name}"

    response = client.get("http://testserver/greet/John")
    assert response.status_code == 200
    assert response.text == "Hello, John"

def test_class_based_handler(api, client):
    class Handler:
        def get(self, req, resp):
            resp.text = "Class Based Handler"

    api.add_route("/class_based", Handler)

    response = client.get("http://testserver/class_based")
    assert response.status_code == 200
    assert response.text == "Class Based Handler"
