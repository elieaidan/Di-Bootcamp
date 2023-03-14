from django.db import models
from country_list import countries_for_language
countries = countries_for_language("en")

categories_list = [("action","action"), ("adventure","adventure"), ("comedy","comedy"), ("drama","drama"), ("fantasy","fantasy"), ("horror","horror"), ("musicals","musicals"), ("mystery","mystery"), ("romance","romance"), ("science-fiction","science-fiction"),  ("sports","sports"), ("thriller","thriller"), ("Western","Western")]

class Country(models.Model):
    name = models.CharField(max_length=5,choices=countries, blank=True, null=True)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, choices=categories_list)
    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
  

class Film(models.Model):
    title= models.CharField(max_length=50)
    release_date = models.DateField()
    date_added = models.DateField(auto_now=True)
    created_in_country = models.ManyToManyField(Country, related_name='films_created')
    available_in_countries = models.ManyToManyField(Country, related_name='films_available')
    category = models.ManyToManyField(Category, related_name='films')
    director =  models.ManyToManyField(Director, related_name='films')

    def __str__(self):
        return self.title

