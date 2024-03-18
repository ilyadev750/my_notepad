from django.urls import path
from .views import (anonymous_note, get_user_notes,
                    new_user_note, update_user_note,
                    delete_user_note, success)


urlpatterns = [
    path("create/", anonymous_note, name="anonymous_note"),
    path("success/<str:message>/", success, name="success"),
    path("<str:username>/", get_user_notes, name="get_user_notes"),
    path("<str:username>/create/", new_user_note, name="new_user_note"),
    path("<str:username>/<slug:slug>/", update_user_note,
         name="update_user_note"),
    path("<str:username>/<slug:slug>/delete", delete_user_note,
         name="delete_user_note"),
]
