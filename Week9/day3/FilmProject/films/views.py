from django.shortcuts import render
from django.views.generic import FormView
from .forms import AddFilmForm, AddDirectorForm
from .models import Film


class AddFilmView(FormView):
    form_class = AddFilmForm
    template_name = 'add_film.html'

    
class AddDirectorView(FormView):
    form_class = AddDirectorForm
    template_name = 'add_director.html'

def films_list(request):
    films = Film.objects.all()
    context = {'films': films }
    return render(request, 'homepage.html', context)


    
