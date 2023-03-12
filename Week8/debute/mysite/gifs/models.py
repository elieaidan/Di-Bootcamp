from django.db import models

# Create your models here.
class Gif (models.Model):
    title = models.CharField(max_length=50),
    url = models.URLField(),
    uploader_name = models.CharField(),
    created_at = models.DateField(auto_now_add=True)

class Category (models.Model):
    name = models.CharField(max_length=50),
    gifs = models.ManyToManyField(Gif, related_name='gifs')








