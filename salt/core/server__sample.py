#Server

from http import server
from typing import Any
from wsgiref.simple_server import make_server
import unittest
  

def core_app(env, start_response):
    if not env:
        return 'The environment dictionary is empty.'.encode('utf-8')

    response_body = [
            f'{key}: {value}' for key, value in sorted(
                env.items()
            )
        ]

    response_body = "\n".join(response_body)

    status = '200 OK'
    
    response_headers = [
        ('Content-type', 'text/html')
    ]
    start_response(status, response_headers)
    return [response_body.encode('utf-8')] 


class Reverseware:
    '''
    This class reverse the data stream.
    '''
    def __init__(self, app):
        self.wrapped_app = app
    
    def __call__(self, env, start_response, *args, **kwargs):
        wrapped_app_response = self.wrapped_app(env, start_response)
        print([data[::-1] for data in wrapped_app_response])
        return [data[::-1] for data in wrapped_app_response]

server = make_server('localhost',8000, app=Reverseware(core_app))
print(f'Server is running... in {8000}')
server.serve_forever()

