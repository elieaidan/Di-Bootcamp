from django.shortcuts import render
from .models import Rental, Customer

def list_rental(request):
    rental_list = Rental.objects.all().order_by('rental_date')
    context = {'rental': rental_list}
    return render(request, 'rental.html', context)

def customer_info(request, get_id):
    customer_details = Customer.objects.get(id=get_id)
    

    
