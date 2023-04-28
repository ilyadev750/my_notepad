from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from note.views import anonymous_note, start, user_note
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', start, name='start'),
    path('base/', anonymous_note, name='anonymous_note'),
    path('admin/', admin.site.urls),
    path('base/users/', include('django.contrib.auth.urls')),
    path('base/users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
