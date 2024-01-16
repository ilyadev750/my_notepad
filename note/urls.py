from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import anonymous_note

urlpatterns = [
    path("", anonymous_note, name="anonymous_note"),
    path("base/users/", include("users.urls")),
    path("admin/", admin.site.urls),
]