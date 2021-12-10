from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_403_FORBIDDEN,
    HTTP_405_METHOD_NOT_ALLOWED,
)

from products.models import Product
from user.models import User
from collections import OrderedDict


class ProductsTestCase(TransactionTestCase):
    fixtures = ["users.json", "categories.json", "products.json"]

    def test_get_products_list(self):
        expected_data = [
            OrderedDict(
                [
                    ("pk", 1),
                    ("category", {"pk": 1, "title": "Category_1"}),
                    ("title", "Product_1"),
                    ("slug", "prod1"),
                    ("description", "Some description for product_1"),
                    ("price", "123.54"),
                    ("in_stock", 5),
                    ("image", None),
                ]
            ),
            OrderedDict(
                [
                    ("pk", 2),
                    ("category", {"pk": 2, "title": "Category_2"}),
                    ("title", "Product_2"),
                    ("slug", "prod2"),
                    ("description", "Some description for product_2"),
                    ("price", "54.13"),
                    ("in_stock", 2),
                    ("image", None),
                ]
            ),
            OrderedDict(
                [
                    ("pk", 3),
                    ("category", {"pk": 3, "title": "Category_3"}),
                    ("title", "Product_3"),
                    ("slug", "prod3"),
                    ("description", "Some description for product_3"),
                    ("price", "178.23"),
                    ("in_stock", 3),
                    ("image", None),
                ]
            ),
            OrderedDict(
                [
                    ("pk", 4),
                    ("category", {"pk": 4, "title": "Category_4"}),
                    ("title", "Product_4"),
                    ("slug", "prod4"),
                    ("description", "Some description for product_4"),
                    ("price", "89.43"),
                    ("in_stock", 0),
                    ("image", None),
                ]
            ),
        ]
        response = self.client.get(reverse("product:list"))
        self.assertListEqual(
            response.data["results"],
            expected_data,
            "Response data not equal expected data.",
        )
        self.assertEqual(response.data["count"], 4)

    def test_get_products_list_with_filter(self):
        expected_data = [
            OrderedDict(
                [
                    ("pk", 1),
                    ("category", {"pk": 1, "title": "Category_1"}),
                    ("title", "Product_1"),
                    ("slug", "prod1"),
                    ("description", "Some description for product_1"),
                    ("price", "123.54"),
                    ("in_stock", 5),
                    ("image", None),
                ]
            )
        ]
        url = f'{reverse("product:list")}?search=Product_1'
        response = self.client.get(url)
        self.assertEqual(
            response.data["results"],
            expected_data,
            "Response data with filters not equal expected data.",
        )

    def test_create_product_anonymous(self):
        url = reverse("product:list")
        data = {
            "category": 4,
            "title": "Product_5",
            "slug": "product5",
            "description": "some description for product_5",
            "price": 65.31,
            "available": True,
            "in_stock": 5,
            "image": "",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

    def test_create_product_admin(self):
        expected_data = {
            "pk": 5,
            "category": {"pk": 4, "title": "Category_4"},
            "title": "Product_5",
            "slug": "product5",
            "description": "some description for product_5",
            "price": "421.22",
            "in_stock": 3,
            "image": None,
        }
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        url = reverse("product:admin-create-product")
        data = {
            "category": 4,
            "title": "Product_5",
            "slug": "product5",
            "description": "some description for product_5",
            "price": "421.22",
            "in_stock": 3,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(response.data, expected_data)

    def test_create_product_user(self):
        user = User.objects.get(pk=2)
        self.client.force_login(user)
        url = reverse("product:list")
        data = {
            "category": 4,
            "title": "Product_5",
            "slug": "product5",
            "description": "some description for product_5",
            "price": 65.31,
            "available": True,
            "in_stock": 5,
            "image": "",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_product_anonymous(self):
        url = reverse("product:product-retrieve-update-destroy", kwargs={"pk": 3})
        data = {
            "pk": 3,
            "category": 3,
            "title": "Product_3",
            "slug": "product3",
            "description": "another description for product_3",
            "price": 111.11,
            "available": False,
            "in_stock": 0,
            "image": "",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_update_product_user(self):
        user = User.objects.get(pk=2)
        self.client.force_login(user)
        url = reverse("product:product-retrieve-update-destroy", kwargs={"pk": 3})
        data = {
            "pk": 3,
            "category": 3,
            "title": "Product_3",
            "slug": "product3",
            "description": "another description for product_3",
            "price": 567.22,
            "available": False,
            "in_stock": 0,
            "image": "",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_update_product_admin(self):
        expected_data = {
            "pk": 3,
            "category": {"pk": 3, "title": "Category_3"},
            "title": "Product_3",
            "slug": "prod3",
            "description": "Some description for product_3",
            "price": "421.54",
            "in_stock": 10,
            "image": None,
        }
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        url = reverse("product:product-retrieve-update-destroy", kwargs={"pk": 3})
        data = {
            "category": 3,
            "title": "Product_3",
            "slug": "prod3",
            "description": "Some description for product_3",
            "price": "421.54",
            "in_stock": 10,
        }
        response = self.client.patch(url, data, content_type="application/json")
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_destroy_product_anonymous(self):
        url = reverse("product:product-retrieve-update-destroy", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_destroy_product_user(self):
        user = User.objects.get(pk=2)
        self.client.force_login(user)
        url = reverse("product:product-retrieve-update-destroy", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_destroy_product_admin(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        url = reverse("product:product-retrieve-update-destroy", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(pk=1).exists())
