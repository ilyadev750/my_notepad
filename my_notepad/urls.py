from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from note.views import note, start


urlpatterns = [
    path('', start, name='start'),
    path('admin/', admin.site.urls),
    path('note/', note, name='note')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
