from django.shortcuts import render
from .models import Rental, Customer, Vehicle
from .forms import CustomerForm, VehicleForm

def list_rental(request):
    rental_list = Rental.objects.all().order_by('rental_date')
    context = {'rental': rental_list}
    return render(request, 'rental.html', context)

def customers(request):
    customer_list = Customer.objects.all().order_by('first_name', 'last_name')
    context = {'customers': customer_list}
    return render(request, 'customers.html', context)

def customer(request, id):
    customer_obj = Customer.objects.get(id=id)
    context = {'customer': customer_obj}
    return render (request, 'customer.html', context)

def add_customer(request):

    if request.method == 'POST':
        form_filled = CustomerForm(request.POST)
        form_filled.save()

    form = CustomerForm()
    context=  {'form': form}

    return render (request, 'add_customer.html', context)


def vehicles(request):
    vehicle_list = Vehicle.objects.all()
    print(vehicle_list)
    context = {'vehicle_list': vehicle_list}
    return render(request, 'vehicles.html', context)

def vehicle(request, id):
    customer_obj = Vehicle.objects.get(id=id)
    context = {'vehicle': vehicle}
    return render (request, 'vehicle.html', context)



def add_vehicle(request):

    if request.method == 'POST':
        form_filled = VehicleForm(request.POST)
        form_filled.save()

    form =  VehicleForm()
    context=  {'form': form}

    return render (request, 'add_vehicle.html', context)