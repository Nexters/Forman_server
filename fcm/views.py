from django.http import Http404
from pyfcm import FCMNotification
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from .models import FcmUsers, FcmMessageHistory
from django.contrib.auth.models import User
import json

# 이슈
## 성공, FCM 전송 테스트하기
## 성공, 응답값 저장 로직 구현하기
## 대기, Response Error 해결하기

# Init
API_KEY = 'AAAAX9tNUgw:APA91bGJ6BWulg_JqGwtHeRffcGnrzkzaQbI-13yRltNIAID6i87_r629r3eg1USzRc86dTnd4WYf3TpWe3mQ66vvOWjzfrcO1dNHRke7dCiGc2GJ3aG7owVJc7b7hO-cue8sAboTGKC'
push_service = FCMNotification(api_key=API_KEY)

# test data
data_message = {
    "title" : "test_title",
    "body" : "test_body"
}

# test user
user = User.objects.filter(username='admin')
fcmUser = FcmUsers.objects.filter(user= user)[0]
token = fcmUser.token
flag = fcmUser.useYN

# test api
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def sendMessages_test(request):

    # fcm_flag = Fcm.objects.filter(token=token)['useYN']
    # if fcm_flag: (True일 때 아래와 같은 로직 수행)
    if flag:
        result = push_service.notify_single_device(
            registration_id = token,
            data_message = data_message,
        )

    success = result['success']
    if success == 1:
        result_message = 'Success'
    else:
        result_message = result['results'][0]['error']

    print(result_message)

    try:
        saveFcmHistory(fcmUser, data_message, result_message)

    except Fcm.DoesNotExist | IndexError:
        saveFcmHistory(fcmUser, data_message, result_message)
        raise Http404("존재하지 않는 FCM 토큰입니다.")

    print(result)

    return Response(result)

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
def saveFcmHistory(fcmUser, data, resultMsg):
    history = FcmMessageHistory()
    history.receiver = fcmUser
    history.sentData = data
    history.resultMsg = resultMsg
    history.save()