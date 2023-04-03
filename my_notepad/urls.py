from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from note.views import note, start
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('home/', cache_page(60)(note), name='note'),
    path('admin/', admin.site.urls),
    path('note/', note, name='note'),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
