from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import anonymous_note, get_user_notes, new_user_note, update_user_note, delete_user_note

urlpatterns = [
    path("create/", anonymous_note, name="anonymous_note"),
    path("<str:username>/", get_user_notes, name="get_user_notes"),
    path("<str:username>/create/", new_user_note, name="new_user_note"),
    path("<str:username>/<slug:slug>/", update_user_note, name="update_user_note"),
    path("<str:username>/<slug:slug>/delete", delete_user_note, name="delete_user_note"),
    # path("admin/", admin.site.urls),
    
]