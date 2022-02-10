import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    username = models.CharField(max_length=30, unique=True)
    email_address = models.EmailField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    profile_picture = models.URLField(blank=True, null=True)

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username