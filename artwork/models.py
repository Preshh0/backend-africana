from time import time
from django.db import models
from django.utils import timezone
# Create your models here.

class Artwork(models.Model):
    art = models.ImageField(max_length=None)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    creator = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    

    class Meta:
        ordering = ["created_at"]