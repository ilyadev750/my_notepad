from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main import views
from note.views import anonymous_note, about


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", about, name="about"),
    path("base/", anonymous_note, name="anonymous_note"),
    path("base/users/", include("users.urls")),
    path("admin/", admin.site.urls),
]
