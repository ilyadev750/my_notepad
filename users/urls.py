from django.urls import path
from .views import login_user, logout_user, register_user
from note.views import new_user_note, get_user_notes, update_user_note, delete_user_note
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login_user/", login_user, name="login"),
    path("logout_user/", logout_user, name="logout"),
    path("register_user/", register_user, name="register"),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="password/password_reset.html"
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("<int:user_id>/", get_user_notes, name="get_user_notes"),
    path(
        "<int:user_id>/<str:type_of_note>/create/", new_user_note, name="new_user_note"
    ),
    path(
        "<int:user_id>/<str:title>/<int:note_id>/update/",
        update_user_note,
        name="update_note",
    ),
    path(
        "<int:user_id>/<str:title>/<int:note_id>/delete/",
        delete_user_note,
        name="delete_note",
    ),
]
