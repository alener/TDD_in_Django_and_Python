from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page #1

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  #2
        self.assertEqual(found.func, home_page)  #3


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  #1
        response = home_page(request)  #2
        self.assertTrue(response.content.startswith(b'<html>'))  #3
        self.assertIn(b'<title>To-Do lists</title>', response.content)  #4
        self.assertTrue(response.content.endswith(b'</html>'))  #5