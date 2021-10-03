from django.contrib.auth.models import User
from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_200_OK


class CurrentUserTestcase(TransactionTestCase):
    fixtures = ["user.json"]

    def setUp(self):
        self.url = reverse("user")
        self.user = User.objects.get(pk=1)

    def test_get_current_user_failed(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_get_current_user_success(self):
        self.client.force_login(self.user)
        expected_data = {
            "username": "SerhiiSliadniev",
            "email": "slplspsp@gmail.com",
            "first_name": "Serhii",
            "last_name": "Sliadniev",
        }
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_update_current_user_failed(self):
        response = self.client.update(self.user)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_update_current_user_success(self):
        self.client.force_login(self.user)
