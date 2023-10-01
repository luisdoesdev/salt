# Api
from cgitb import handler
from email.policy import default
from typing import Any
from urllib import request, response
from webob import Request, Response


class API:
    def __init__(self) -> None:
        self.routes = {}
    
    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        
        return wrapper

    def default_response(self, response):
        response.status = "404"
        response.text = "Not found"
    
    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            if path == request_path:
                return handler
       

    def handle_request(self, request):
        user_agent = request.environ.get('HTTP_USER_AGENT', 'No User Agent Found')

        response = Response()

        handler = self.find_handler(request_path=request.path)

        if handler is not None:
            handler(request, response)
        else:
            self.default_response(response)
       
        # response.text = f"Hello, my friend with user agent: {user_agent}"
        return response