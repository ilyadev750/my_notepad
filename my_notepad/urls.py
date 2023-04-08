from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from note.views import note, start
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', start, name='start'),
    path('home/', note, name='note'),
    # add url for each user
    path('admin/', admin.site.urls),
    path('home/users/', include('django.contrib.auth.urls')),
    path('home/users/', include('users.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
