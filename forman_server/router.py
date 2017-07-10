from rest_framework import routers
from api.rest_api import ApiConfigViewSet

router = routers.DefaultRouter()
router.register(r'api', ApiConfigViewSet)
