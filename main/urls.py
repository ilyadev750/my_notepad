from django.urls import path
from .views import index, about, send_mail


urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("send_mail/", send_mail, name="send_mail"),
]
