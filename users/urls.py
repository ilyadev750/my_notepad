from django.urls import path
from note.views import new_user_note, get_user_notes, update_user_note, delete_user_note
from django.contrib.auth import views as auth_views
from .views import login_user, logout_user, register_user, UserForgotPasswordView, UserPasswordResetConfirmView

urlpatterns = [
    path("login/", login_user, name="login"),
    path("logout_user/", logout_user, name="logout"),
    path("registration/", register_user, name="registration"),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
