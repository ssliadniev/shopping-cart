from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name="Peter", last_name="John", phone='123456789')

    def test_string_method(self):
        student = User.objects.get(id=1)
        expected_string = f"{student.first_name}, {student.last_name}"
        self.assertEqual(str(student), expected_string)

    def test_get_absolute_url(self):
        student = User.objects.get(id=1)
        self.assertEqual(student.get_absolute_url(), "/user/1")
