from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page #1

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  #2
        self.assertEqual(found.func, home_page)  #3


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  #1
        response = home_page(request)  #2
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string('home.html',
            {'new_item_text':  'A new list item'}
            )

        self.assertEqual(response.content.decode(), expected_html)

        

        #self.assertTrue(response.content.strip().startswith(b'<html>'))  #3
        #self.assertIn(b'<title>To-Do lists</title>', response.content)  #4
        #self.assertTrue(response.content.strip().endswith(b'</html>'))
