from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.status import (HTTP_200_OK, HTTP_201_CREATED,
                                   HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED)

from products.models import Category
from user.models import User


class CategoriesTestCase(TransactionTestCase):
    categories_fixtures = ["categories.json"]
    users_fixtures = ["users.json"]

    def test_category_list_to_return_success(self):
        expected_data = [{"pk": "1", "title": "Category_1"}]
        response = self.client.get(reverse("product:category"))
        self.assertListEqual(
            response.data, expected_data, "Response data not equal expected data."
        )

    def test_category_list_with_filter_to_return_success(self):
        expected_data = [{"pk": "1", "title": "Category_1"}]
        url = f'{reverse("product:category")}?search=qwe'
        response = self.client.get(url)
        self.assertListEqual(
            response.data, expected_data, "Response data not equal expected data."
        )

    def test_create_category_anonymous(self):
        url = reverse("product:category", kwargs={"pk": 1})
        data = {"title": "category_5", "slug": "categ5"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        url = reverse("product:category", kwargs={"pk": 1})
        data = {"title": "category_5", "slug": "categ5"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(response.data, {})

    def test_create_user_to_return_success(self):
        user = User.objects.get(pk=2)
        self.client.force_login(user)
        url = reverse("product:category", kwargs={"pk": 1})
        data = {"title": "category_5", "slug": "categ5"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_retrieve_category(self):
        response = self.client.get(reverse("product:category"))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data["count"], 4)

    def test_update_category_anonymous(self):
        url = reverse("product:category", kwargs={"pk": 1})
        data = {"title": "category_1", "slug": "categ1"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_update_category_user(self):
        user = User.objects.get(pk=2)
        self.client.force_login(user)
        url = reverse("product:category", kwargs={"pk": 1})
        data = {"title": "category_1", "slug": "categ1"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_update_category_admin(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        url = reverse("product:category", kwargs={"pk": 1})
        data = {"title": "category_1", "slug": "categ1"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, {})

    def test_destroy_category_anonymous(self):
        url = reverse("product:category", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_destroy_category_user(self):
        user = User.objects.get(pk=2)
        self.client.force_login(user)
        url = reverse("product:category", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_destroy_category_admin(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        url = reverse("product:category", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(pk=1).exists())
