import unittest
from core.api import API
import logging


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.api = API()

    def test_handle_request(self):
        class MockRequest:
            environ = {'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        expected_response_text = "Hello, my friend with user agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        response = self.api.handle_request(MockRequest())
        self.assertEqual(response.text, expected_response_text)
    
    def test_route_decorator(self):
        '''
        Test the functionality of the route decorator by adding routes to 
        the API instance and printing the current routes.
        
        It's interactive as well, so you can play around with it.
        
        '''
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.debug('Starting test_route_decorator')
        def add_route(route_names):
            if len(route_names) == 0:
                return
            for route_name in route_names:
                @self.api.route(f'/{route_name}')
                def route_function(request, response):
                    response.text = {route_name}
                    logging.info(f'Response text set to {response.text}')

        route_names = ['home','about'] # feel free to add remove route names
        add_route(route_names)
        logging.debug(f'This are the current routes: {self.api.routes.keys()}')
   

if __name__ == '__main__':
    unittest.main()