from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_401_UNAUTHORIZED,
)

from products.models import Product
from user.models import User


class CategoriesTestCase(TransactionTestCase):
    products_fixtures = ["products.json"]
    users_fixtures = ["users.json"]

    def test_products_list_to_return_success(self):
        expected_data = [
            {
                "pk": "1",
                "category": "Category_1",
                "title": "Product_1",
                "slug": "product1",
                "description": "some description for product_1",
                "price": "132.32",
                "available": True,
                "in_stock": "3",
                "image": "",
            },
            {
                "pk": "2",
                "category": "Category_2",
                "title": "Product_2",
                "slug": "product2",
                "description": "some description for product_2",
                "price": "423.12",
                "available": False,
                "in_stock": "0",
                "image": "",
            },
        ]
        response = self.client.get(reverse("product"))
        self.assertListEqual(
            response.data, expected_data, "Response data not equal expected data."
        )

    def test_products_list_with_filter_to_return_success(self):
        expected_data = [
            {
                "pk": "1",
                "category": "Category_1",
                "title": "Product_1",
                "slug": "product1",
                "description": "some description for product_1",
                "price": "132.32",
                "available": True,
                "in_stock": "3",
                "image": "",
            }
        ]
        url = f'{reverse("product")}?search=available'
        response = self.client.get(url)
        self.assertListEqual(
            response.data, expected_data, "Response data not equal expected data."
        )

    def test_create_product_anonymous(self):
        url = reverse("product", kwargs={"pk": 3})
        data = {
            "pk": "3",
            "category": "Category_3",
            "title": "Product_3",
            "slug": "product3",
            "description": "some description for product_3",
            "price": "23.31",
            "available": True,
            "in_stock": "5",
            "image": "",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_create_product_admin(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        url = reverse("product:category", kwargs={"pk": 3})
        data = {
            "pk": "3",
            "category": "Category_3",
            "title": "Product_3",
            "slug": "product3",
            "description": "some description for product_3",
            "price": "23.31",
            "available": True,
            "in_stock": "5",
            "image": "",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(response.data, {})

    def test_create_user_to_return_success(self):
        user = User.objects.get(pk=2)
        self.client.force_login(user)
        url = reverse("product:category", kwargs={"pk": 3})
        data = {
            "pk": "3",
            "category": "Category_3",
            "title": "Product_3",
            "slug": "product3",
            "description": "some description for product_3",
            "price": "23.31",
            "available": True,
            "in_stock": "5",
            "image": "",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_retrieve_category(self):
        response = self.client.get(reverse("product:category"))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)

    def test_update_category_anonymous(self):
        url = reverse("product:category", kwargs={"pk": 3})
        data = {
            "pk": "3",
            "category": "Category_3",
            "title": "Product_3",
            "slug": "product3",
            "description": "some description for product_3",
            "price": "23.31",
            "available": True,
            "in_stock": "5",
            "image": "",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_update_category_user(self):
        user = User.objects.get(pk=2)
        self.client.force_login(user)
        url = reverse("product:category", kwargs={"pk": 3})
        data = {
            "pk": "3",
            "category": "Category_3",
            "title": "Product_3",
            "slug": "product3",
            "description": "some description for product_3",
            "price": "23.31",
            "available": True,
            "in_stock": "5",
            "image": "",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_update_product_admin(self):
        user = Product.objects.get(pk=1)
        self.client.force_login(user)
        url = reverse("product", kwargs={"pk": 3})
        data = {
            "pk": "3",
            "category": "Category_3",
            "title": "Product_3",
            "slug": "product3",
            "description": "some description for product_3",
            "price": "23.31",
            "available": True,
            "in_stock": "5",
            "image": "",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, {})

    def test_destroy_product_anonymous(self):
        url = reverse("product", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_destroy_product_user(self):
        user = Product.objects.get(pk=1)
        self.client.force_login(user)
        url = reverse("product", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_destroy_product_admin(self):
        user = Product.objects.get(pk=1)
        self.client.force_login(user)
        url = reverse("product", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(pk=1).exists())
