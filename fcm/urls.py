from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^send', views.sendMessages_test),
]
