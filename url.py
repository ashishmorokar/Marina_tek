from django.contrib import admin
from django.urls import path
from movies.views import movie_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', movie_list, name='movie_list'),
    # Add other URL patterns as needed
]
