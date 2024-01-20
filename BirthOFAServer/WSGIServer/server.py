import os
from wsgiref.simple_server import make_server


class Reverseware:
    def __init__(self, app):
        self.wrapped_app = app

    def __call__(self, environ, start_response, *args, **kwargs):
        wrapped_app_response = self.wrapped_app(environ, start_response)
        return [data[::-1] for data in wrapped_app_response]


def application(environ, start_response):
    # response_body = [
    #     f'{key}: {value}' for key, value in sorted(environ.items())
    # ]
    # response_body = '\n'.join()
    response_body = render_html()

    status = '200 OK'

    response_headers = [
        # ('Content-type', 'text/plain'),
        ('Content-type', 'html')
    ]

    start_response(status, response_headers)

    return [response_body.encode('utf-8')]

def render_html():
    ROOT = os.getcwd()
    PATH = '/birth_of_a_server/WSGIServer/templates'
    # def read_and_join_lines(file_path):
    file_path = f'{ROOT}{PATH}/index.html'
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            # Join the lines into a single string
            content = ''.join(lines)

            return content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


server = make_server('localhost', 8000, app=application)
server.serve_forever()
# print(application("", []))