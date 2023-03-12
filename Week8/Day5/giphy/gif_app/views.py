from django.shortcuts import render
from .models import Category, Gif
from .forms import CategoryForm

# Create your views here.

def homepage(request):

    gifs_all = Gif.objects.all()
    context = {'gifs': gifs_all}

    return render(request, 'homepage.html', context)

def category(request, id:int):

    category_specific = Category.objects.get(id=id)
    category_gifs = category_specific.gifs.all()

    context = {'category': category_specific, 'gifs': category_gifs}

    return render(request, 'category.html', context)

def categories(request):
    
    categories_all = Category.objects.all()
    form = CategoryForm
    context = {'categories': categories_all, 'form': form}

    return render(request, 'categories.html', context)