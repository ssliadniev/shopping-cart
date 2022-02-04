from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_403_FORBIDDEN,
    HTTP_405_METHOD_NOT_ALLOWED,
)
from user.models import User
from decimal import Decimal
from collections import OrderedDict


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

    def test_get_carts_login_user(self):
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
            response.data["result"]["count"], 1, "Number of carts not equal 1."
        )
        self.assertEqual(
            response.data["total_amount"],
            expected_total_amount,
            "Response total amount not equal expected total amount.",
        )

    def test_create_cart_item_anonymous(self):
        url = reverse("cart:cart_item_update_destroy", kwargs={"pk": 1})
        data = {
            "cart": 3,
            "product": 3,
            "quantity": 6
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_create_cart_item_login_user(self):
        url = reverse("cart:cart_item_update_destroy", kwargs={"pk": 1})
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        data = {
            "cart": 1,
            "product": 3,
            "quantity": 6
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)


