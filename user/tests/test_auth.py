from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_405_METHOD_NOT_ALLOWED


class AuthTest(TransactionTestCase):

    def setUp(self):
        self.login_url = reverse("login")
        self.register_url = reverse("register")

    def test_register_successful(self):
        data = {
            "username": "Serhii",
            "email": "slplspsp@gmail.com",
            "password1": "12345qwerty",
            "password2": "12345qwerty"
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_register_failed(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)

    def test_login_successful(self):
        login_data = {
            "username": "admin",
            "password": "admin"
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_login_failed(self):
        login_data = {
            "username": "noadmin",
            "password": "noadmin"
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, HTTP_405_METHOD_NOT_ALLOWED)
