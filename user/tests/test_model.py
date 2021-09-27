from django.test import TransactionTestCase
from django.contrib.auth.models import User
from django.db import models
from user.views import CurrentUserRetrieveUpdateAPIView


class UserModelTestcase(TransactionTestCase):

    def test_current_user(self):
        # get current user endpoint (view)
        # check
        pass

    def test_update_current_user(self):

        pass
