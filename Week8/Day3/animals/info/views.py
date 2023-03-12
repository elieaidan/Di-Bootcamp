from django.shortcuts import render
from .models import Family, Animal


def animals_list(request):
    animals = Animal.objects.all()
    context = {'animals': animals}

    return render(request, 'animals.html', context)


def family_list(request):
    families = Family.objects.all()
    context = {'families': families}

    return render(request, 'families.html', context)

def animal(request, id:int): 
    animal_specific = Animal.objects.get(id=id)
    context = {'animal': animal_specific}

    return render(request, 'animal.html', context)

def family(request, id:int):
    family_specific = Family.objects.get(id=id)
    family_animals = family_specific.animal_set.all()

    context = {'family': family_specific, 'animals': family_animals}

    return render(request, 'family.html', context)