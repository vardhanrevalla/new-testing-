from unittest import skip
from importlib import import_module

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from Storage.models import Category, Product
from Storage.views import product_all



@skip("demonstrating skipping for future look back")
class TestSkip(TestCase):
    def test_skip_example(self):
        pass


class TestViewResponses(TestCase):

    def setUp(self):
        self.c = Client()
        # self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='test', slug='test')
        Product.objects.create(category_id=1, title='product test', created_by_id=1,
                               slug='product-test', price='100.00', image='sampleimg')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        :return: None
        """
        response = self.c.get('/',HTTP_HOST='randomaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/',HTTP_HOST='bookstore.com')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        """
        Test homepage response status
        :return: None
        """
        response = self.c.get('/')

    def test_product_detail_url(self):
        """
        Test individual product view response status
        :return: None
        """
        response = self.c.get(reverse('Storage:product_detail', args=['product-test']))
        self.assertEqual(response.status_code, 200)

    def test_category_list_url(self):
        """
        Test category view response status
        :return: None
        """
        response = self.c.get(reverse('Storage:category_list', args=['test']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Test homepage content
        :return:
        """
        request = HttpRequest()

        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()

        response = product_all(request)
        html = response.content.decode('utf8')
        self.assertIn('<a class="dropdown-item" href="/shop/test/">', html)
        self.assertIn('<title>BookStore</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    # def test_view_function(self):
    #     """
    #     Trying out requestFactory
    #     :return:
    #     """
    #     request = self.factory.get('/')
    #     response = product_all(request)
    #     html = response.content.decode('utf8')
    #     self.assertIn('<a class="dropdown-item" href="/shop/test/">', html)
    #     self.assertIn('href="/product-test/">product test</a>', html)
    #     self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
