from django.contrib import admin
from .models import Customer, VehicleSize, VehicleType, Vehicle, Rental, RentalRate

admin.site.register(Customer)
admin.site.register(Vehicle)
admin.site.register(Rental)
