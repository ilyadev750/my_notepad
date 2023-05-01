from django.urls import path, re_path
from .views import login_user, logout_user, register_user
from note.views import new_user_note, get_user_notes, update_user_note

urlpatterns = [
    path('login_user/', login_user, name="login"),
    path('logout_user/', logout_user, name="logout"),
    path('register_user/', register_user, name="register_user"),
    path('<item>/', new_user_note,  name="new_user_note"),
    # path('current/id1/', get_user_notes, name='us'),
    re_path(r"^current/id(?P<id>[0-9]{1,7})/$", get_user_notes, name='back'),
    re_path(r"^current/id(?P<id>[0-9]{1,7})/(?P<slug>[\w-]+)/$", update_user_note),
]