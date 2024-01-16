from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import index, about

urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
]