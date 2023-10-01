#App
import unittest
from urllib import response
from api import API

app = API()

# add route handling
def home(request, response):
    response.text = "hello"


