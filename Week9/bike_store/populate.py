import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
import django
django.setup()

from rent.models import Customer
from faker import Faker

fake = Faker(locale=['en_US', 'fr_FR', 'it_IT'])

# exeple de fonction pour ajouter des faker avec le nombre que je choisit dans ma fonction

def create_customers(number:int):
    for _ in range(number):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone_number = fake.msisdn()
        address= fake.address()

        customer = Customer(first_name = first_name, 
                            last_name = last_name,
                            email= email, 
                            phone_number = phone_number,
                            address = address)

        customer.save()

    print(f"CREATED {number}")


create_customers(100)