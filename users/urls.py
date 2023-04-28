from django.urls import path, re_path
from .views import login_user, logout_user, register_user
from note.views import user_note, get_user_notes

urlpatterns = [
    path('login_user/', login_user, name="login"),
    path('logout_user/', logout_user, name="logout"),
    path('register_user/', register_user, name="register_user"),
    path('', user_note, name="user_note"),
    # re_path(r"^id(?P<id>[+][0-9]+)/(?P<slug>[\w]+)/$", user_note)
    re_path(r"^id(?P<id>[0-9]{1,7})/$", get_user_notes),
]