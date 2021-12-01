from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_403_FORBIDDEN,
)

from products.models import Category
from user.models import User
from collections import OrderedDict


class CategoriesTestCase(TransactionTestCase):
    fixtures = ["users.json", "categories.json"]

    def test_category_list(self):
        expected_data = [
            OrderedDict([("pk", 1), ("title", "Category_1"), ("slug", "categ1")]),
            OrderedDict([("pk", 2), ("title", "Category_2"), ("slug", "categ2")]),
            OrderedDict([("pk", 3), ("title", "Category_3"), ("slug", "categ3")]),
            OrderedDict([("pk", 4), ("title", "Category_4"), ("slug", "categ4")]),
        ]
        response = self.client.get(reverse("product:category-list-create"))
        self.assertEqual(
            response.data["results"],
            expected_data,
            "Response data not equal expected data.",
        )

    def test_category_list_with_filter(self):
        expected_data = [
            OrderedDict([("pk", 2), ("title", "Category_2"), ("slug", "categ2")])
        ]
        url = f'{reverse("product:category-list-create")}?search=Category_2'
        response = self.client.get(url)
        self.assertEqual(
            response.data["results"],
            expected_data,
            "Response data not equal expected data.",
        )

    def test_create_category_anonymous(self):
        url = reverse("product:category-retrieve-update-destroy", kwargs={"pk": 1})
        data = {"title": "category_5", "slug": "categ5"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_create_category_admin(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        url = reverse("product:category-list-create")
        data = {"pk": 5, "title": "category_5", "slug": "categ5"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    def test_create_category_user(self):
        user = User.objects.get(pk=2)
        self.client.force_login(user)
        url = reverse("product:category-retrieve-update-destroy", kwargs={"pk": 1})
        data = {"title": "category_5", "slug": "categ5"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_get_list_of_category(self):
        response = self.client.get(reverse("product:category-list-create"))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["count"], 4)

    def test_update_category_anonymous(self):
        url = reverse("product:category-retrieve-update-destroy", kwargs={"pk": 1})
        data = {"title": "category_1", "slug": "categ1"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_update_category_user(self):
        user = User.objects.get(pk=2)
        self.client.force_login(user)
        url = reverse("product:category-retrieve-update-destroy", kwargs={"pk": 1})
        data = {"title": "category_1", "slug": "categ1"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_update_category_admin(self):
        expected_data = {"pk": 1, "title": "category_1", "slug": "categ1"}
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        url = reverse("product:category-retrieve-update-destroy", kwargs={"pk": 1})
        data = {"title": "category_1", "slug": "categ1"}
        response = self.client.patch(url, data, content_type="application/json")
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_destroy_category_anonymous(self):
        url = reverse("product:category-retrieve-update-destroy", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_destroy_category_user(self):
        user = User.objects.get(pk=2)
        self.client.force_login(user)
        url = reverse("product:category-retrieve-update-destroy", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_destroy_category_admin(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        url = reverse("product:category-retrieve-update-destroy", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(pk=1).exists())
