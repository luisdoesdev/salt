#App
from api import API

app = API()


@app.route('/home')
def home(request, response):
    response.text = "hello"

# Uncomment this to see the error: AssertionError("Route exists")

# @app.route('/home')
# def home(request, response):
#     response.text = "hello"


@app.route('/about')
def about(request, response):
    response.text = "about page"

@app.route('/hello/{name}')
def greeting(request, response, name):
    response.text = f"hello, {name}"

@app.route("/sum/{num_1:d}/{num_2:d}")
def sum(request, response, num_1, num_2):
    total = int(num_1) + int(num_2)
    response.text = f"{num_1} + {num_2} = {total}"

@app.route("/book")
class BooksResource:
    def get(self, req, resp):
        resp.text = "Books Page"
    
    def post(self, req,resp):
        resp.text = "Endpoint to create a book"
