import requests

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from xmljson import parker
from xml.etree.ElementTree import fromstring
from django.shortcuts import get_object_or_404

from .models import ApiService, ApiHeader, ApiServiceParams, ApiToken, ApiParams


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

    print(response.content)
    print(response.status_code)
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


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_execute(request, api, service):
    api_service = get_object_or_404(ApiService, name=service, api__name=api, useYN=True)

    response = None
    header_params = {}
    request_params = {}
    data_params = {}

    # API의 Header를 세팅한다
    api_headers = ApiHeader.objects.filter(api=api_service.api)

    for api_header in api_headers:
        if api_header.valueType == 99:
            apiToken = ApiToken.objects.filter(api=api_service.api, name=api_header.value,
                                               isDev=api_service.api.type)
            header_params[api_header.key] = apiToken[0].token
        else:
            header_params[api_header.key] = api_header.value

    # 아래의 파라미터 세팅을 모듈화 시켜 보자
    # API의 공통 파라미터를 세팅한다
    apiParams = ApiParams.objects.filter(api=api_service.api)

    for api_service_param in apiParams:
        if api_service_param.reqMethod == 0:
            if api_service_param.valueInputType == 0:
                request_params[api_service_param.key] = request.GET.get(api_service_param.key, '')
            elif api_service_param.valueInputType == 1 and api_service_param.valueType == 99:
                apiToken = ApiToken.objects.filter(api=api_service.api, name=api_service_param.value, isDev=api_service.api.type)
                request_params[api_service_param.key] = apiToken[0].token
            else:
                request_params[api_service_param.key] = api_service_param.value
        else:
            if api_service_param.valueInputType == 0:
                data_params[api_service_param.key] = request.GET.get(api_service_param.key, '')
            elif api_service_param.valueInputType == 1 and api_service_param.valueType == 99:
                apiToken = ApiToken.objects.filter(api=api_service.api, name=api_service_param.value,
                                                   isDev=api_service.api.type)
                data_params[api_service_param.key] = apiToken[0].token
            else:
                if api_service_param.valueType == 1:
                    data_params[api_service_param.key] = int(api_service_param.value)
                else:
                    data_params[api_service_param.key] = api_service_param.value


    # API의 Request를 설정한다
    api_service_params = ApiServiceParams.objects.filter(api=api_service)

    for api_service_param in api_service_params:
        if api_service_param.reqMethod == 0:
            if api_service_param.valueInputType == 0:
                request_params[api_service_param.key] = request.GET.get(api_service_param.key, '')
            elif api_service_param.valueInputType == 1 and api_service_param.valueType == 99:
                apiToken = ApiToken.objects.filter(api=api_service.api, name=api_service_param.value, isDev=api_service.api.type)
                request_params[api_service_param.key] = apiToken[0].token
            else:
                if api_service_param.valueType == 1:
                    request_params[api_service_param.key] = int(api_service_param.value)
                else:
                    request_params[api_service_param.key] = api_service_param.value
        else:
            if api_service_param.valueInputType == 0:
                data_params[api_service_param.key] = request.GET.get(api_service_param.key, '')
            elif api_service_param.valueInputType == 1 and api_service_param.valueType == 99:
                apiToken = ApiToken.objects.filter(api=api_service.api, name=api_service_param.value, isDev=api_service.api.type)
                data_params[api_service_param.key] = apiToken[0].token
            else:
                if api_service_param.valueType == 1:
                    data_params[api_service_param.key] = int(api_service_param.value)
                else:
                    data_params[api_service_param.key] = api_service_param.value


    # API의 Post 데이터를 설정한다

    print(api_service.reqUrl, header_params, request_params, data_params)

    if api_service.reqMethod == 0:
        response = requests.get(url=api_service.reqUrl, headers=header_params, params=request_params)
    else:
        response = requests.post(url=api_service.reqUrl, headers=header_params, data=data_params, params=request_params)

    print(response.url)
    print(response.content)

    if api_service.resType == 1:
        return Response(parker.data(fromstring(response.content)))

    return Response(response.json())
