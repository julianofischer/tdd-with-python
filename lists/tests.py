from django.http import HttpRequest
from django.urls import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from lists.views import home_page
# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        # html = response.content.decode('utf-8')
        # expected_html = render_to_string('lists/home.html')
        self.assertTemplateUsed(response, 'lists/home.html')