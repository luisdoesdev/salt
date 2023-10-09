import pytest
from salt.salt import SALT


FILE_DIR = "css"
FILE_NAME = "main.css"
FILE_CONTENTS = '''element{
    --garlic-theme-color:  rgb(136, 95, 66);
}
a {color: var(--garlic-theme-color);}'''
def _create_static(static_dir):
    asset = static_dir.mkdir(FILE_DIR).join(FILE_NAME)
    asset.write(FILE_CONTENTS)

    return asset


# Fixture for the SALT instance
@pytest.fixture
def api():
    app = SALT()

    @app.route('/home')
    def home(request, response):
        response.text = "hello"

    @app.route('/about')
    def about(request, response):
        response.text = "about page"

    @app.route('/hello/{name}')
    def greeting(request, response, name):
        response.text = f"hello, {name}"

    route_name = "car"

    @app.route(f'/{route_name}')
    class BooksResource:
        def get(self, req, resp):
            resp.text = f"{route_name.capitalize()} Page"

        def post(self, req, resp):
            resp.text = f"Endpoint to create a {route_name.capitalize()}"

    return app

# Fixture for the test client
@pytest.fixture
def client(api):
    return api.test_client()

def test_home_route(client):
    response = client.get('http://testserver/home')
    assert response.text == "hello"
    assert response.status_code == 200

def test_about_route(client):
    response = client.get('http://testserver/about')
    assert response.text == "about page"
    assert response.status_code == 200

def test_greeting_route(client):
    response = client.get('http://testserver/hello/John')
    assert response.text == "hello, John"
    assert response.status_code == 200

def test_books_get(client):
    route_name = "car"
    response = client.get(f'http://testserver/{route_name}')
    assert response.text == f"{route_name.capitalize()} Page"
    assert response.status_code == 200

def test_books_post(client):
    route_name = "car"
    response = client.post(f'http://testserver/{route_name}')
    assert response.text == f"Endpoint to create a {route_name.capitalize()}"
    assert response.status_code == 200

def test_alternative_route(api, client):
    response_text = 'This is test illustrating an alternative way to add routes'

    def home(req, resp):
        resp.text = response_text

    api.add_route("/alternative", home)
    response = client.get('http://testserver/alternative')
    assert response.text == response_text
    assert response.status_code == 200

def test_template(api, client):
    @api.route("/html")
    def html_handler(req, resp):
        resp.body = api.template("index.html", context={"title": "Response Title", "name": "Response Text"}).encode()

    response = client.get('http://testserver/html')
    assert "text/html" in response.headers["Content-Type"]
    assert "Response Title" in response.text
    assert "Response Text" in response.text

def test_custom_exception_handler(api, client):
    def on_exception(req, resp, exc):
        resp.text = "AttributeErrorHappened"

    api.add_exception_handler(on_exception)

    @api.route("/")
    def index(req, resp):
        raise AttributeError()

    response = client.get("http://testserver/")

    assert response.text == "AttributeErrorHappened"

def test_404_is_returned_for_nonexistent_static_file(client):
    assert client.get(f"http://testserver/main.css)").status_code == 404

def test_assets_are_served(tmpdir_factory):
    api = SALT()
    client = api.test_client()
    response = client.get(f"http://testserver/{FILE_NAME}")
    assert response.status_code == 200
    assert response.text == FILE_CONTENTS