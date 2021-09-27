from django.test import TransactionTestCase
from django.test import Client
from django.contrib.auth.models import User
from django.db import models
from user.views import CurrentUserRetrieveUpdateAPIView


class UserModelTestcase(TransactionTestCase):
    fixtures = ["user.json"]

    def test_current_user(self):
        #user = User.objects.get(pk=1)
        #self.assertEqual(user.first_name, "Serhii")
        pass
    def test_update_current_user(self):

        pass
