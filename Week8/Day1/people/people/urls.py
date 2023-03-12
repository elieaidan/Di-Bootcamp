
from django.contrib import admin
from django.urls import path
from people_app.views import people_list

urlpatterns = [
    path('admin/', admin.site.urls),

]
