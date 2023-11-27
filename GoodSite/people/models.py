from django.db import models

# Create your models here.
data_db = []


class Students(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, blank=True, db_index=True)
