from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def some_text(request):
    """Shows text on screen"""
    return HttpResponse('Some Text')

def about(request):
    return HttpResponse('<h1>Welcome Users<h1>')

def posts(request):
    all_posts = Post.objects.all()
    context = {'posts': all_posts}

    return render(request, 'posts.html', context)