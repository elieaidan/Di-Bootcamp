from django.contrib import admin
from django.urls import path, include
from gif_app.views import homepage, category, categories

urlpatterns = [
    path("__reload__/", include("django_browser_reload.urls")),
    path("admin/", admin.site.urls),
    path("homepage/", homepage, name="homepage"),
    path("category/<int:id>", category, name="category"),
    path("categories/", categories)
]

