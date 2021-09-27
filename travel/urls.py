from django.contrib import admin
from django.template import base
from django.urls import path, include

from travel.vievs import home, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include('cities.urls', 'cities')),
    path('home/', home),
    path('about/', about),
]
