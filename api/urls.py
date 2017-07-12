from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^kml', views.kml),
    url(r'^ex/terminal', views.experessBusTerminal),
]