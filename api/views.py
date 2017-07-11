import requests

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Apiconfig


#######################################################################################################################
# author : 진재언
# API : 시작점과 도착점의 위도, 경도 데이터를 추출하여 최적의 경로와 소요 시간을 반환
#
# description
#  : 사용자의 주소를 입력하면, 위도, 경도를 반환하는 API를 GET 방식으로 호출한다.
#  : 호출한 API가 데이터(위도, 경도)를 가져온다.
#  : 위에서 받은 데이터(시작점과 도착점에 대한 위도, 경도)를 통해 최적의 경로와 소요 시간을 반환한다.
#
# 추가 및 수정할 부분
# (추가) 현재는 한 가지 주소에 대한 위도, 경도 데이터를 가져오기만 한다. 두 지점의 위도/경도를 가져오자
# (추가) 두 지점의 위도/경도를 이용하여 경로 및 소요시간을 가져오자.
#
# issue
#  : 예외처리 안했음 ( 200성공/실패, 400잘못된요청 등.. )
#  : 도로명주소, 기존주소 동적? 정적?
#  : json에서 key로 value 가져오는 건 어떻게 할까?~
#  : 주현이가 설정한 restframework url? 이게 뭔지 물어보고 namespace에 대해서도..
#######################################################################################################################
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def geoCoding(request):
    # 파라미터 저장
    # version = request.GET.get('version', "1")
    city_do = request.GET.get('city_do', "empty")
    gu_gun = request.GET.get('gu_gun', "empty")
    dong = request.GET.get('dong', 'empty')
    bunji = request.GET.get('bunji', 'empty')
    detailAddress = request.GET.get('detailAddress', 'empty')
    # addressFlag = request.GET.get('addressFlag', 'F02')
    # coordType = request.GET.get('coordType', 'WGS84GEO')

    # 헤더 설정
    headers = {
        'Content-Type': 'application/json',
        'appKey': Apiconfig.objects.filter(name='tmap', type=0)[0].token,  # 향후 모듈화 시킨다
    }

    # 파라미터 설정
    requestParam = {
        'version': '1',  # tmap api version, 1
        'city_do': city_do,  # 시/도 명칭
        'gu_gun': gu_gun,  # 구/군 명칭
        'dong': dong,  # F01-동 명칭, F02-도로명 명칭
        'bunji': bunji,  # 출력 좌표에 해당하는 지번
        'detailAddress': detailAddress,  # 상세 주소
        'addressFlag': 'F02',  # F01-지번주소타입, F02-새주소타입
        'coordType': 'WGS84GEO',  # 좌표 타입, 위도경도 > WGS84GEO
    }

    # 요청 URL
    requestUrl = "https://apis.skplanetx.com/tmap/geo/geocoding"

    # 응답 객체
    response = requests.get(requestUrl, headers=headers, params=requestParam)

    data = response.json()
    print(data['coordinateInfo']['addressFlag'])

    # print("STATUS : " + str(response.status_code))

    return Response(response.json())
