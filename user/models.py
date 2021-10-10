from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=70, blank=True, null=True)
    photo = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"
