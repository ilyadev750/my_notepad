from django.urls import path
from note.views import new_user_note, get_user_notes, update_user_note, delete_user_note
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView, PasswordChangeDoneView
from .views import login_user, logout_user, register_user, UserForgotPasswordView, UserPasswordResetConfirmView, UserPasswordChangeView

urlpatterns = [
    path("login/", login_user, name="login"),
    path("logout_user/", logout_user, name="logout"),
    path("registration/", register_user, name="registration"),

    path("<str:username>/change-password", UserPasswordChangeView.as_view(), name='password_change'),
    path("<str:username>/change-password/done", PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change'),
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
