
from django.contrib import admin
from django.urls import path
from films.views import AddDirectorView, AddFilmView, films_list 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_director/', AddDirectorView.as_view(), name='add_director'),
    path('add_film/', AddFilmView.as_view(), name='add_film'),
    path('homepage/', films_list, name='homepage')
   
]
