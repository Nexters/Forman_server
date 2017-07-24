from pyfcm import FCMNotification
from .models import Fcm, FcmMessageHistory

# 이슈
## 테스트 해보기

# init
API_KEY = ""
push_service = FCMNotification(api_key="")

# 메세지 전송
def sendMessages(receivers, title, body):
    for i in receivers:
        result = push_service.notify_single_device(
            registration_id = receivers[i],
            message_title = title,
            message_body= body
        )
        saveFcmHistory(result['results'], title, body)

# 보낸 메세지 저장
def saveFcmHistory(resultCode, title, body):
    history = FcmMessageHistory()
    history.sentData = {'title': title, 'body': body}
    history.resultCode = resultCode
    history.save()

