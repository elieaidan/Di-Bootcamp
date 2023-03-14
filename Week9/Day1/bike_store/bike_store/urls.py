
from django.contrib import admin
from django.urls import path
from rent.views import customers, customer, add_customer,vehicles, vehicle, add_vehicle,RentalListView,RentalDetailsViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', customers),
    path('customer/<int:id>', customer, name='customer'),
    path('add_customer/', add_customer),
    path('vehicles/', vehicles),
    path('vehicle/<int:id>', vehicle, name='vehicle'),
    path('add_vehicle/', add_vehicle),
    path('rentals/', RentalListView.as_view()),
    path('rental/<int:pk>', RentalDetailsViews.as_view(), name = 'rental')


  ]
