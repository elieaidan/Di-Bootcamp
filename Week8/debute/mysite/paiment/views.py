from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    user = {
        'first_name' : "John",
        'last_name' : "Doe"
    } 

    subjects = [
        {
            'title' : "How to setup Django",
            'author': "Maria"
        },
        {
            'title' : "How to cake an amazing pie",
            'author' : "Chef Mark"
        }
    ]

    context = {
        'user' : user,
        'subjects': subjects
    }
    return render(request, 'index.html', context)