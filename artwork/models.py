from unicodedata import category
import uuid
from datetime import datetime
from django.db import models
from accounts.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name




class Artwork(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    art = models.URLField(blank=True, null=True)
    slug = models.SlugField(max_length=200, db_index=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=300)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    created_at = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey(Category, related_name='artwork', on_delete=models.CASCADE)    

    class Meta:
        ordering = ["created_at"]