
import os
import unittest
from app import app

class BaseTestCase(unittest.TestCase):
  """ Base Tests """

  def setUp(self):
    self.app = app.test_client()
    self.app.testing = True 

  def tearDown(self):
    pass

  def test_main_page_is_reachable(self):
    response = self.app.get('/', follow_redirects=True)
    self.assertEqual(response.status_code, 200)


class HelloWorldTestCase(unittest.TestCase):
  """ Base Tests """

  def setUp(self):
    self.app = app.test_client()
    self.app.testing = True 

  def tearDown(self):
    pass

  def test_hello_world_response(self):
    response = self.app.get('/index', follow_redirects=True)
    self.assertEqual(response.data, b"Hello world")
