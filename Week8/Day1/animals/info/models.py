from django.db import models


class Animal(models.Model):
    
    legs  = models.BigIntegerField()
    weight = models.BigIntegerField()
    height   = models.BigIntegerField()
    speed   = models.BigIntegerField()
    family = models.TextField(max_length=5)
