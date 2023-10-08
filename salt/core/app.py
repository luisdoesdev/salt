#App
from core.api import API

TEMPLATE = "templates" # TODO: remove the need for 'core' in the path
app = API(templates_dir=TEMPLATE)


@app.route('/home')
def home(request, response):
    response.text = "hello"


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

def alternative_routing(req, resp):
    resp.text = "sample"

app.add_route("/sample", alternative_routing)

@app.route("/template")
def template_handler(req, resp):
    resp.text = app.template("index.html", context={"name": "Template Name", "name": "Salt Framework"})
