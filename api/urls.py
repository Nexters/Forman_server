from django.conf.urls import url
from . import views
from .models import ApiService

urlpatterns = [
    url(r'^kml', views.kml),
    url(r'^ex/terminal', views.experessBusTerminal),
    url(r'^(?P<api>[-\w]+)/(?P<service>[-\w]+)', views.api_execture)
]
