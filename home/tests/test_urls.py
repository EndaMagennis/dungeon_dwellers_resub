from django.test import SimpleTestCase


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        # This test checks if the URL / is resolved to the view index in the home app.
        response = self.client.get('/')
        # The response should be 200, which means the view was found.
        self.assertEqual(response.status_code, 200)
        # The view should use the template home/index.html.
        self.assertTemplateUsed(response, 'home/index.html')