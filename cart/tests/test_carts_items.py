from collections import OrderedDict
from decimal import Decimal

from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.status import (HTTP_200_OK, HTTP_204_NO_CONTENT,
                                   HTTP_403_FORBIDDEN, HTTP_404_NOT_FOUND)

from cart.models import CartItem
from user.models import User


class CategoriesTestCase(TransactionTestCase):

    fixtures = [
        "users.json",
        "products.json",
        "categories.json",
        "carts.json",
        "carts_items.json",
    ]

    def test_get_cart_items_anonymous(self):
        response = self.client.get(reverse("cart:cart_item_list_create"))
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_get_cart_items_login_user(self):
        expected_data = [
            OrderedDict(
                [
                    ("cart", 1),
                    ("product", {"pk": 1, "title": "Product_1", "image": None}),
                    ("quantity", 13),
                    ("sub_total", Decimal("1606.02")),
                ]
            ),
        ]
        expected_total_amount = Decimal("1606.02")
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        response = self.client.get(reverse("cart:cart_item_list_create"))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertListEqual(
            response.data["result"]["results"],
            expected_data,
            "Response data not equal expected data.",
        )
        self.assertEqual(
            response.data["total_amount"],
            expected_total_amount,
            "Response total amount not equal expected total amount.",
        )

    def test_update_cart_item_anonymous(self):
        url = reverse("cart:cart_item_update_destroy", kwargs={"pk": 1})
        data = {"cart": 1, "product": 3, "quantity": 6}
        response = self.client.patch(url, data, content_type="application/json")
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_update_cart_item_login_user(self):
        expected_data = {
            "cart": 1,
            "product": {"pk": 1, "title": "Product_1", "image": None},
            "quantity": 4,
            "sub_total": Decimal("494.16"),
        }
        url = reverse("cart:cart_item_update_destroy", kwargs={"pk": 1})
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        data = {"cart": 1, "product": 2, "quantity": 4}
        response = self.client.patch(url, data, content_type="application/json")
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_update_cart_item_for_another_user(self):
        url = reverse("cart:cart_item_update_destroy", kwargs={"pk": 1})
        user = User.objects.get(pk=2)
        self.client.force_login(user)
        data = {"cart": 1, "product": 3, "quantity": 20}
        response = self.client.patch(url, data, content_type="application/json")
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_destroy_cart_item_anonymous(self):
        url = reverse("cart:cart_item_update_destroy", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_destroy_cart_item_user(self):
        user = User.objects.get(pk=2)
        self.client.force_login(user)
        url = reverse("cart:cart_item_update_destroy", kwargs={"pk": 2})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertFalse(CartItem.objects.filter(pk=2).exists())

    def test_destroy_cart_item_admin(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        url = reverse("cart:cart_item_update_destroy", kwargs={"pk": 1})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertFalse(CartItem.objects.filter(pk=1).exists())

    def test_destroy_cart_item_for_another_user(self):
        user = User.objects.get(pk=3)
        self.client.force_login(user)
        url = reverse("cart:cart_item_update_destroy", kwargs={"pk": 2})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
