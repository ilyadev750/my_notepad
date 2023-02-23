from django.contrib import admin
from django.urls import path

from article.views import index, note


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('note/', note, name='note')
]
