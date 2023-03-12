from django.db import models
from django.utils import timezone

# Create your models here.

class Customer (models.Model):
    first_name= models.CharField(max_length=50)
    last_name=  models.CharField(max_length=50)
    email= models.EmailField()
    phone_number= models.CharField(max_length=50)
    address= models.CharField(max_length=50)
    city= models.CharField(max_length=50)
    country= models.CharField(max_length=50)

class VehicleType(models.Model):
    name = models.CharField(max_length=50)  


class VehicleSize(models.Model):
    name = models.CharField(max_length=50)   

       

class Vehicle(models.Model):
    vehicle_type= models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    date_created= models.DateTimeField(default=timezone.now)
    real_cost= models.IntegerField()
    size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)


class Rental(models.Model):
    rental_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle =  models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class RentalRate(models.Model):
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)