import unittest
from urllib import response

from app import app



class CoronaTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    # tests to see if all the new routes are working
    def test_search_visitors_page(self):
        response = self.app.get('/search_visitors', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_agent_visitor_info_page(self):
        response = self.app.get('/agent_visitor_info', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_agent_search_hospitals_page(self):
        response = self.app.get('/agent_search_hospitals', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_agent_search_places_page(self):
        response = self.app.get('/agent_search_places', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_hospital_register_page(self):
        response = self.app.get('/hospital_register', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_hospital_DB_status_change_page(self):
        response = self.app.get('/hospital_DB_status_change', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_scan_QR_page(self):
        response = self.app.get('/scan-QR', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_visitor_check_out_page(self):
        response = self.app.get('/visitor_check_out', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # testing ability for hospital to change visitor status
    def test_hospital_DB_status_change_work(self): # changing a test visitor's status to infected
        response = self.app.post(
            '/hospital_DB_status_change', data=dict(fname="Tfname", lname="Tlname", status="1") ,follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    


    



    

if __name__ == "__main__":
    unittest.main()