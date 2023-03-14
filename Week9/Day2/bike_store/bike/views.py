from django.shortcuts import render
from .models import Customer, Rental
from .forms import CustomerForm, RentalForm
from django.views.generic import ListView, DetailView, FormView

def customers(request): 
    customers_list = Customer.objects.all().order_by('first_name', 'last_name')
    context = {'customers': customers_list}
    return render(request, 'customers.html', context)


def customer(request, id:int):
    customer_obj = Customer.objects.get(id=id)
    context = {'customer': customer_obj}
    return render(request, 'customer.html', context)

def add_customer(request):

    if request.method == 'POST':
        form_filled = CustomerForm(request.POST)
        form_filled.save()

    form = CustomerForm()
    context = {'form': form}
    return render(request, 'add_customer.html', context)

class RentalListView(ListView): # gets list of all objects of a model
    model = Rental
    template_name = 'rentals.html'
    context_object_name = 'rentals'

class RentalDetailView(DetailView): # gets one specific object of a model
    model = Rental
    template_name = 'rental.html'
    context_object_name = 'rental'

    def get_context_data(self, **kwargs): # allows to modify the context dictionary
        context = super().get_context_data(**kwargs)
        customer = self.get_object().customer # self.get_object() returns the specific object (Rental)
        vehicle = self.get_object().vehicle
        context['customer'] = customer
        context['vehicle'] = vehicle
        return context
    
class RentalFormView(FormView):
    form_class = RentalForm
    template_name = 'add_rental.html'
    
    