from django.db import models
from django.utils import timezone
from country_list import countries_for_language

countries = countries_for_language("en")

# Create your models here.

class Customer (models.Model):
    first_name= models.CharField(max_length=200)
    last_name=  models.CharField(max_length=200)
    email= models.EmailField()
    phone_number= models.CharField(max_length=200)
    address= models.CharField(max_length=200)
    city= models.CharField(max_length=50, blank= True, null=True)
    country= models.CharField(max_length=5, choices=countries, blank= True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name}, {self.last_name}'

class VehicleType(models.Model):

    vehicle_types = [
        ('C', 'City'),
        ('D', 'Dirt'),
        ('El', 'Electric')
    ]

    name = models.CharField(max_length=2, choices=vehicle_types)  

    def __str__(self) -> str:
        return self.name


class VehicleSize(models.Model):

    vehicle_size = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    ]
    name = models.CharField(max_length=2, choices=vehicle_size) 

    def __str__(self) -> str:
        return self.name  

       

class Vehicle(models.Model):
    type= models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    date_created= models.DateTimeField(auto_now_add=True)
    real_cost= models.DecimalField(max_digits=5, decimal_places=2)
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.type}, {self.size},{self.real_cost}'


class Rental(models.Model):
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null= True, auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle =  models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f'{self.vehicle}, {self.customer}'



class RentalRate(models.Model):
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)