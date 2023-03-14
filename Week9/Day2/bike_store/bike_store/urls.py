from django.contrib import admin
from django.urls import path
from bike.views import (customers, 
                        customer, 
                        add_customer, 
                        RentalListView, 
                        RentalDetailView,
                        RentalFormView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("customers/", customers, name='customers'),
    path("customer/<int:id>", customer, name='customer'),
    path("add_customer/", add_customer),
    path("rentals/", RentalListView.as_view(), name='rentals'),
    path("rental/<int:pk>", RentalDetailView.as_view(), name='rental'),
    path("add_rental/", RentalFormView.as_view())
]
