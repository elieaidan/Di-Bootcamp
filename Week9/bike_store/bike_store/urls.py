
from django.contrib import admin
from django.urls import path
from rent.views import customers, customer, add_customer,vehicles, vehicle, add_vehicle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', customers),
    path('customer/<int:id>', customer, name='customer'),
    path('add_customer/', add_customer),
    path('vehicles/', vehicles),
    path('vehicle/<int:id>', vehicle),
    path('add_vehicle/', add_vehicle, name='vehicle'),
  ]
