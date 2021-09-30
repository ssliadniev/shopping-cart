from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED,  HTTP_201_CREATED


class AuthTest(TransactionTestCase):

    def test_register_successful(self):
        register_url = reverse("register")
        response = self.client.get(register_url)
        self.assertEqual(response.status_code, HTTP_200_OK)