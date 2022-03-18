import os
import sys
import unittest
from flaskext.mysql import MySQL
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from app import app

class TestCases(unittest.TestCase):

    #test for landing page
    def test_landing_page(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type="html/text")
        self.assertIn(b'Visitor Registration', response.data)

    def test_visitor_registration(self):
        self.assertIn()

if __name__=='__main__':
   unittest.main()