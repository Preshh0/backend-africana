from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    username = models.CharField(max_length=10)
    email_address = models.EmailField()
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.username