import unittest
from webob import Request
from api import API

class TestAPIRoutes(unittest.TestCase):
    """
    Test the features of the API class.
        This module contains unit tests for the API 
        class in the api.py file. It tests the functionality of the API class by 
        simulating requests to the routes defined in the class. The tests include testing the home route, 
        about route, and greeting route. The simulate_request method is used to simulate requests to the routes, 
        and the test_client method is used to test the responses. The test cases include checking if the response text and status are correct.  
    """
    def setUp(self):
        self.api = API()

        @self.api.route('/home')
        def home(request, response):
            response.text = "hello"

        @self.api.route('/about')
        def about(request, response):
            response.text = "about page"

        @self.api.route('/hello/{name}')
        def greeting(request, response, name):
            response.text = f"hello, {name}"

    def simulate_request(self, path):
        environ = {
            'REQUEST_METHOD': 'GET',
            'PATH_INFO': path,
            'wsgi.url_scheme': 'http',
            'wsgi.input': b""
        }
        return self.api.test_client(environ)

    def test_home_route(self):
        response = self.simulate_request('/home')
        self.assertEqual(response.text, "hello")
        self.assertEqual(response.status, "200 OK")

    def test_about_route(self):
        response = self.simulate_request('/about')
        self.assertEqual(response.text, "about page")
        self.assertEqual(response.status, "200 OK")

    def test_greeting_route(self):
        response = self.simulate_request('/hello/John')
        self.assertEqual(response.text, "hello, John")
        self.assertEqual(response.status, "200 OK")

if __name__ == "__main__":
    unittest.main()


            