from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
# Create your models here.

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class AddPictures(models.Model):
    image = models.ImageField(_("Image"), upload_to =upload_to,  default="posts/default.jpg")
    date_added = models.DateField()
    time_added = models.TimeField(default=timezone.now)
    user_info = models.CharField(max_length=255)
    image_title = models.CharField(max_length=255)
