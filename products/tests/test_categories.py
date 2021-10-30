from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from products.models import Category


class CategoriesTestCase(TransactionTestCase):

    def setUp(self):
        self.url = reverse("category")
        self.category = Category.objects.get(pk=1)

    def test_get_category_failed(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_get_category_success(self):
        pass
