
from faker import Faker
fake = Faker()

namefake = fake.name()


adressfake = fake.address()



dic1 = []
def users(**kwargs):
    dic1.append(kwargs)

users (name = namefake, adress = adressfake)
print(dic1)





