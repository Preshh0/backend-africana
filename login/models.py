from django.db import models
from django.db.models.fields import CharField
from django.utils import timezone
# Create your models here.

class UserProfile(models.Model):
    userImage = models.ImageField(upload_to="profileImage")
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    # username = models.CharField(max_length=255)
    pictures = models.ImageField(upload_to="pictures")
    password = models.CharField(max_length=255, default=timezone.now)