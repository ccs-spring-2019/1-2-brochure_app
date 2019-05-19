from django.test import SimpleTestCase  # using SimpleTestCase isntead of TestCase because we're not using a database

# python manage.py test to run tests


class SimpleTestCase(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # 200 is standard response for a successful HTTP request

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
