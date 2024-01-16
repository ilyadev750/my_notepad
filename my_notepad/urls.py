from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from main import views
from note.views import anonymous_note, about


urlpatterns = [
    path("", include("main.urls")),
    path("notes/", include("note.urls")),
    path("base/users/", include("users.urls")),
    path("admin/", admin.site.urls),
]
