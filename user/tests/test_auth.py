from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED,  HTTP_201_CREATED


class AuthTest(TransactionTestCase):

    def test_register_successful(self):
        data = {
            ""
        }
        register_url = reverse("register")
        response = self.client.post(register_url, data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_register_failed(self):
        data = {
            ""
        }
        register_url = reverse("register")
        response = self.client.post(register_url, data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_login_successful(self):
        pass

    def test_login_failed(self):
        pass
