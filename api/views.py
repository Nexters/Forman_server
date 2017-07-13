import requests

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from xmljson import parker
from xml.etree.ElementTree import fromstring

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
        'appKey': '',
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

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def experessBusTerminal(request):
    terminal_name = request.GET.get("tmNm", None)

    params = {
        'serviceKey': '',
        'tmnNm': terminal_name
    }

    request_url = 'http://openapi.tago.go.kr/openapi/service/ExpBusArrInfoService/getExpBusTmnList'

    response = requests.get(url=request_url, params=params)

    print(response.content)
    return Response(parker.data(fromstring(response.content)))
