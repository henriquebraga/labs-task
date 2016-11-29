from django.test import TestCase


class IndexViewTest(TestCase):
    """Tests for index page."""

    def setUp(self):
        self.resp = self.client.get('/')

    def test_get(self):
        """GET must return status code 200."""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Response must use template index.html."""
        self.assertTemplateUsed(self.resp, 'index.html')

class IndexNotFoundTest(TestCase):
    """Tests for invalid page."""

    def setUp(self):
        self.resp = self.client.get('/anything')

    def test_get(self):
        """GET must return status code 404."""
        self.assertEqual(404, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, '404.html')



