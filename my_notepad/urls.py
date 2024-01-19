from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main import views



urlpatterns = [
    path("", include("main.urls")),
    path("", include("users.urls")),
    path("notes/", include("note.urls")),
    path("admin/", admin.site.urls),
]
