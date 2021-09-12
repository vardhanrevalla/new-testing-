from django.contrib.auth.models import User
from django.test import TestCase

from Storage.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name="test", slug="test")

    def test_categories_model_entry(self):
        """
        Test the category model data insertion/types/field attribs
        :return: None
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_categories_model_entry(self):
        """
        Test the category model default name
        :return: None
        """
        data = self.data1
        self.assertEqual(str(data), "test")


class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='test', slug='test')
        User.objects.create(username='admin')
        self.product1 = Product.objects.create(category_id=1, title='product test', created_by_id=1,
                                               slug='product-test', price='100.00', image='sampleimg')

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attribs
        :return:None
        """
        data = self.product1
        self.assertTrue(isinstance(data, Product))

    def test_categories_model_entry(self):
        """
        Test the product model default name
        :return: None
        """
        data = self.product1
        self.assertEqual(str(data), 'product test')
