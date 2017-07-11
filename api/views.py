import requests

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Apiconfig


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def kml(request):
    # 데이터 저장
    endX = request.GET.get('endX', "empty")
    endY = request.GET.get('endY', "empty")
    startX = request.GET.get('startX', 'empty')
    startY = request.GET.get('startY', 'empty')

    # 헤더 설정
    headers = {
        'Content-Type': 'application/json',
        'appKey': Apiconfig.objects.filter(name='tmap', type=0)[0].token,  # 향후 모듈화 시킨다
    }

    # 파라미터 설정
    # requestParam = {
    #    'version': '1',  # tmap api version, 1
    # }

    # 페이로드 설정
    payload = {
        'startX': startX,
        'startY': startY,
        'endX': endX,
        'endY': endY,
        'reqCoordType': 'WGS84GEO',
        'resCoordType': 'WGS84GEO'
    }

    # 요청 URL
    request_url = "https://apis.skplanetx.com/tmap/routes?version=1"

    # 응답 객체
    response = requests.post(request_url, params=payload, headers=headers)
    return Response(response.json())
