from django.test import TestCase  # check classes
from django.contrib.auth.models import User


class UserModelTestcase(TestCase):

    def test_current_user(self):
        # get current user endpoint (view)
        # check
        pass

    def test_update_current_user(self):

        pass

    def test_string_method(self):
        student = User.objects.get(id=1)
        expected_string = f"{student.first_name}, {student.last_name}"
        self.assertEqual(str(student), expected_string)

    def test_get_absolute_url(self):
        student = User.objects.get(id=1)
        self.assertEqual(student.get_absolute_url(), "/user/1")
