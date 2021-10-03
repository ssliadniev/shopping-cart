from django.contrib.auth.models import User
from django.test import TransactionTestCase
from django.urls import reverse
from rest_framework.status import HTTP_401_UNAUTHORIZED


class CurrentUserTestcase(TransactionTestCase):
    fixtures = ["user.json"]

    def test_get_current_user_failed(self):
        url = reverse("user")
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)

    def test_get_current_user_success(self):
        expected_data = {}
        # force_login
        # check status.code and check data
        # response.data
        pass

    def test_update_current_user_failed(self):
        pass