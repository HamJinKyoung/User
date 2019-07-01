from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    grade = models.CharField(max_length=1)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.username
