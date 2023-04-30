from django.urls import path, re_path
from .views import login_user, logout_user, register_user
from note.views import new_user_note, get_user_notes, update_user_note

urlpatterns = [
    path('login_user/', login_user, name="login"),
    path('logout_user/', logout_user, name="logout"),
    path('register_user/', register_user, name="register_user"),
    path('', new_user_note, name="user_note"),
    re_path(r"^id(?P<id>[0-9]{1,7})/(?P<slug>[\w-]+)/$", update_user_note),
    re_path(r"^id(?P<id>[0-9]{1,7})/$", get_user_notes),
]