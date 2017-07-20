import requests

from xmljson import parker
from xml.etree.ElementTree import fromstring
from rest_framework import serializers, viewsets
from django.shortcuts import get_object_or_404
from .models import ApiService, ApiHeader, ApiServiceParams, ApiToken, ApiParams

#모듈화 작업필
def get3rd_api(api, service):
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
                apiToken = ApiToken.objects.filter(api=api_service.api, name=api_service_param.value,
                                                   isDev=api_service.api.type)
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
    request_params = setParam(api_service, request, request_params, api_service_params)


    # API의 Post 데이터를 설정한다

    print(api_service.reqUrl, header_params, request_params, data_params)

    if api_service.reqMethod == 0:
        response = requests.get(url=api_service.reqUrl, headers=header_params, params=request_params)
    else:
        response = requests.post(url=api_service.reqUrl, headers=header_params, data=data_params, params=request_params)

    print(response.url)
    print(response.content)

    if api_service.resType == 1:
        return parker.data(fromstring(response.content))

    return response.json()


def setParam(api_service, request_params, org_params, target):
    params_new = {}
    params_new += org_params
    for api_service_param in target:
        if api_service_param.reqMethod == 0:
            if api_service_param.valueInputType == 0:
                params_new[api_service_param.key] = request_params.GET.get(api_service_param.key, '')
            elif api_service_param.valueInputType == 1 and api_service_param.valueType == 99:
                apiToken = ApiToken.objects.filter(api=api_service.api, name=api_service_param.value,
                                                   isDev=api_service.api.type)
                params_new[api_service_param.key] = apiToken[0].token
            else:
                if api_service_param.valueType == 1:
                    params_new[api_service_param.key] = int(api_service_param.value)
                else:
                    params_new[api_service_param.key] = api_service_param.value
        else:
            if api_service_param.valueInputType == 0:
                params_new[api_service_param.key] = request_params.GET.get(api_service_param.key, '')
            elif api_service_param.valueInputType == 1 and api_service_param.valueType == 99:
                apiToken = ApiToken.objects.filter(api=api_service.api, name=api_service_param.value,
                                                   isDev=api_service.api.type)
                params_new[api_service_param.key] = apiToken[0].token
            else:
                if api_service_param.valueType == 1:
                    params_new[api_service_param.key] = int(api_service_param.value)
                else:
                    params_new[api_service_param.key] = api_service_param.value
    return params_new