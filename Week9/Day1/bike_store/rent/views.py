from django.shortcuts import render
from .models import Rental, Customer, Vehicle
from .forms import CustomerForm, VehicleForm
from django.views.generic import ListView, DetailView

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


class RentalListView(ListView): #gets list of all objects of a model
    model = Rental
    template_name = 'rental.html'
    context_object_name = 'rental'

class RentalDetailsViews(DetailView): #gets one specific object of a model
    model = Rental
    template_name= 'rental.html'
    context_object_name= 'rental'

    def get_context_data(self, **kwargs): #allows to modify the content dictionary
        context = super().get_context_data(**kwargs)
        customer = self.get_object().customer
        vehicle = self.get_object().vehicle
        context['customer'] = customer
        context ['vehicle'] = vehicle
        return context