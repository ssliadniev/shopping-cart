from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK


class AuthTest(TransactionTestCase):

    def setUp(self):
        self.url = reverse("login")
        self.register_url = reverse("register")

    def test_register_successful(self):
        data = {
            ""
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_register_failed(self):
        data = {
            ""
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_login_successful(self):
        login_data = {
            "username": "admin",
            "password": "admin"
        }
        response = self.client.post(self.url, login_data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_login_failed(self):
        login_data = {
            "username": "noadmin",
            "password": "noadmin"
        }
        response = self.client.post(self.url, login_data)
        self.assertEqual(response.status_code, HTTP_200_OK)
