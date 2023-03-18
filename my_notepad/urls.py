from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from article.views import index, note


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('note/', note, name='note')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
