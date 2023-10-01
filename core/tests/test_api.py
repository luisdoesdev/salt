import unittest
from core.api import API

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.api = API()

    def test_handle_request(self):
        class MockRequest:
            environ = {'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        expected_response_text = "Hello, my friend with user agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        response = self.api.handle_request(MockRequest())
        self.assertEqual(response.text, expected_response_text)

if __name__ == '__main__':
    unittest.main()