from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from note.views import anonymous_note, start


urlpatterns = [
    path("", start, name="start"),
    path("base/", anonymous_note, name="anonymous_note"),
    path("base/users/", include("users.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
