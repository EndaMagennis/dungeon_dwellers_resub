from django.test import SimpleTestCase


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')