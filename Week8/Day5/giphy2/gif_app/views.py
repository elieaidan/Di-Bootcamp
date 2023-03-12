from django.shortcuts import render
from .models import Category, Gif
from .forms import CategoryForm, GifForm

# Create your views here.

def homepage(request):

    if request.method == 'post':
        form = GifForm(request.POST)
        form.save()


    gifs_all = Gif.objects.all()
    form = GifForm()
    context = {'gifs': gifs_all, 'form': form}

    return render(request, 'homepage.html', context)


def add_like(gif_id):
    gif = Gif.objects.get(id=gif_id)
    gif.likes += 1
    gif.save()

def add_dislike(gif_id):
    gif = Gif.objects.get(id=gif_id)
    gif.likes -= 1
    gif.save()




def category(request, id:int):

    category_specific = Category.objects.get(id=id)
    category_gifs = category_specific.gifs.all()

    data_like = request.GET.get('LIKE')
    if data_like:
        add_like(int(data_like))

    data_dislike = request.GET.get('DISLIKE')
    if data_dislike:
        add_dislike(int(data_dislike))


    context = {'category': category_specific, 'gifs': category_gifs}



    return render(request, 'category.html', context)



def categories(request):
    
    # Request methods
    # GET - getting data
    # POST - changing data

    if request.method == 'POST':
         print("DATA POST:", request.POST)
         form = CategoryForm(request.POST) # after data in form
         form.save()
    

    categories_all = Category.objects.all()
    form = CategoryForm() # empty form 
    context = {'categories': categories_all, 'form': form}

    return render(request, 'categories.html', context)