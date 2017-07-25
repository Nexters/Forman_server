from pyfcm import FCMNotification
from requests import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from .models import Fcm, FcmMessageHistory

# 이슈
## 성공, FCM 전송 테스트하기
## 대기, 응답값 저장 로직 구현하기
## 대기, Response Error 해결하기

# Init
API_KEY = 'AAAAX9tNUgw:APA91bGJ6BWulg_JqGwtHeRffcGnrzkzaQbI-13yRltNIAID6i87_r629r3eg1USzRc86dTnd4WYf3TpWe3mQ66vvOWjzfrcO1dNHRke7dCiGc2GJ3aG7owVJc7b7hO-cue8sAboTGKC'
push_service = FCMNotification(api_key=API_KEY)

# test data
data_message = {
    "title" : "test_title",
    "body" : "test_body"
}

# test token
token = 'd3UDwgG_MvY:APA91bEOwvu3LhJXvqoHlO8hQJruMxUc0o9zLz9HAj84p6sNXvCsh-MROFHDiAPz2ga4GPf7IptE9NaI9MLlOPT7XGgUpoq_STXxG-dH8E76DnPmKx0OvrBBiia6Z9P0mRobY2g1Zez1'

# test api
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def sendMessages_test(request):

    result = push_service.notify_single_device(
        registration_id = token,
        data_message = data_message,
    )

    # Response Data
    result_message = ''
    result_code = ''

    success = result['success']
    if success == 1:
        result_code = 200
        result_message = 'Success'
    else:
        result_code = 000 # 원래 status를 받는게 따로 있었는데 python에는 없네..?
        result_message = result['results'][0]['error']

#   user = Fcm.objects.filter(token=token)
#   saveFcmHistory(user, data_message, result_code, result_message)

    return Response('')

########################################################################################################################

# 메세지 전송
# def sendMessages(receivers, title, body):
#     for i in receivers:
#         result = push_service.notify_single_device(
#             registration_id = receivers[i],
#             message_title = title,
#             message_body= body
#         )
#        # saveFcmHistory(result['results'], title, body)

# 보낸 메세지 저장
# def saveFcmHistory(user, data, resultCode, resultMsg):
#     history = FcmMessageHistory()
#     history = user
#     history.sentData = data
#     history.resultCode = resultCode
#     history.resultMsg = resultMsg
#     history.save()