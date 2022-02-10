import uuid
from datetime import datetime
from django.db import models
from accounts.models import User
# Create your models here.

class Artwork(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    art = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    created_at = models.DateTimeField(default=datetime.now)
    

    class Meta:
        ordering = ["created_at"]