from .models import Apiconfig
from rest_framework import serializers, viewsets


class ApiConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apiconfig
        fields = ('name', 'type', 'token',)


class ApiConfigViewSet(viewsets.ModelViewSet):
    queryset = Apiconfig.objects.all()
    serializer_class = ApiConfigSerializer
