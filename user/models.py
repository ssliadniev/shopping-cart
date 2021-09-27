from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=70)
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
