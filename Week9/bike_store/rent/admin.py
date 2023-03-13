from django.contrib import admin

from .models import Customer, VehicleSize, VehicleType, Vehicle, Rental

admin.site.register(Customer)
admin.site.register(Rental)
admin.site.register(Vehicle)
