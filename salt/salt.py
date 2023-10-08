# Api

import inspect
import os
from re import TEMPLATE
from parse import parse
from webob import Request, Response
from requests import Session as RequestsSession
from wsgiadapter import WSGIAdapter as RequestsWSGIAdapter
from jinja2 import Environment, FileSystemLoader
from wsgiref.simple_server import make_server

TEMPLATE = 'salt/templates'
class SALT: # rename to Salt
    def __init__(self, templates_dir=TEMPLATE) -> None:
        self.routes = {}
        self.templates_env = Environment(
            loader=FileSystemLoader(os.path.abspath(templates_dir))
        )
    
    def __call__(self, environ, start_response):
        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)
    
    def add_route(self, path, handler):
        assert path not in self.routes, "Route exists"
        self.routes[path] = handler
    

    def route(self, path):
        # if path in self.routes:
        #     raise AssertionError("Route exists")
        assert path not in self.routes, "Route exists"

        def wrapper(handler):
            self.routes[path] = handler
            return handler
        
        return wrapper

    def default_response(self, response):
        response.status = "404"
        response.text = "Not found"
    
    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            parse_result = parse(path, request_path)
            if parse_result is not None:
                return handler, parse_result.named # type: ignore check parse library for more info
        return None, None

    def handle_request(self, request):
        
        response = Response()

        handler, kwargs = self.find_handler(request_path=request.path)

        if handler is not None:
            if inspect.isclass(handler):
                handler_function = getattr(handler(), request.method.lower(), None)
                if handler_function is None:
                    raise AttributeError("Method not allowed", request.method)
                
                handler_function(request, response, **kwargs)
            else:
                handler(request, response, **kwargs) # kwargs injects the named parameters from the parse library
        else:
            self.default_response(response)
       
        return response
    
    def test_client(self, base_url="http://testserver"):
        session = RequestsSession()
        session.mount(prefix=base_url, adapter=RequestsWSGIAdapter(self))
        return session
    

    def template(self, template_name, context=None):
        if context is None:
            context = {}

        return self.templates_env.get_template(template_name).render(**context)
    
       
    def app_settings_info(self):
        print(f'''
            TEMPLATE: {TEMPLATE}
        ''')

    def run(self):
        server = make_server("localhost", 8000, self)
        try: 
            print("Server running on port 8000")
            print("Press CTRL + C to close")
            server.serve_forever()
        except KeyboardInterrupt:
            server.shutdown()
            server.server_close()
            print("Server closed")