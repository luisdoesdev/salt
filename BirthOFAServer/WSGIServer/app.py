from core.api import API


app = API()

@app.route("/hello/{name}")
def greeting(request, response, name):
    response.text = f"Hello, {name}"