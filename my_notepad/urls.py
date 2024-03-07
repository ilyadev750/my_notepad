from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", include("main.urls")),
    path("", include("users.urls")),
    path("notes/", include("note.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path(
        'admin/password_reset/', auth_views.PasswordResetView.as_view(),
         name='admin_password_reset'),
    path("admin/", admin.site.urls),
]
