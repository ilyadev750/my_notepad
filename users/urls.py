from django.urls import path, re_path
from .views import login_user, logout_user, register_user
from note.views import new_user_note, get_user_notes, update_user_note, delete_user_note

urlpatterns = [
    path('login_user/', login_user, name="login"),
    path('logout_user/', logout_user, name="logout"),
    path('register_user/', register_user, name="register"),
    path('<int:user_id>/', get_user_notes, name="get_user_notes"),
    path('<int:user_id>/<str:type_of_note>/create/', new_user_note, name="new_user_note"),
    path('<int:user_id>/<str:title>/<int:id>/update/', update_user_note, name='update_note'),
    path('<int:user_id>/<str:title>/<int:id>/delete/', delete_user_note, name='delete_note'),
]