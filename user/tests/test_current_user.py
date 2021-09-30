from django.contrib.auth.models import User
from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK


class CurrentUserTestcase(TransactionTestCase):
    fixtures = ["user.json"]

    def test_get_current_user_success(self):
        url = reverse("user")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_update_current_user_success(self):
        pass
