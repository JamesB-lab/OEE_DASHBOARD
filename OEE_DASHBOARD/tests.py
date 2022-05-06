from urllib import response
from django.test import SimpleTestCase

# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_DA5_page_status_code(self):
        response = self.client.get('/da5/')
        self.assertEqual(response.status_code, 200)

    def test_DA6_page_status_code(self):
        response = self.client.get('/da6/')
        self.assertEqual(response.status_code, 200)

    def test_BB1_page_status_code(self):
        response = self.client.get('/bb1/')
        self.assertEqual(response.status_code, 200)

    def test_BB2_page_status_code(self):
        response = self.client.get('/bb2/')
        self.assertEqual(response.status_code, 200)

    def test_GE3_page_status_code(self):
        response = self.client.get('/ge3/')
        self.assertEqual(response.status_code, 200)

    def test_DA7_page_status_code(self):
        response = self.client.get('/da7/')
        self.assertEqual(response.status_code, 200)