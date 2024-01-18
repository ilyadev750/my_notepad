from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import anonymous_note, get_user_notes

urlpatterns = [
    path("create/", anonymous_note, name="anonymous_note"),
    path("<str:username>/", get_user_notes, name="get_user_notes"),
    path("admin/", admin.site.urls),
    
]