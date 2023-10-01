#App
from api import API

app = API()


@app.route('/home')
def home(request, response):
    response.text = "hello"

@app.route('/about')
def about(request, response):
    response.text = "about page"

