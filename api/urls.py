from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^geocoding$', views.geoCoding),
]