from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models

class FcmUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = '사용자')
    token = models.CharField(max_length=300, verbose_name = 'FCM 토큰')
    useYN = models.BooleanField(default=True, verbose_name='알림 허용')
    createdDate = models.DateTimeField(default=timezone.now, verbose_name='등록일')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = verbose_name_plural = 'FCM 토큰'


class FcmMessageHistory(models.Model):
    receiver = models.ForeignKey(FcmUsers, verbose_name="수신자", on_delete=models.CASCADE)
    sentData = models.TextField(verbose_name="전송 데이터")
    sentDate = models.DateTimeField(default=timezone.now, verbose_name="전송 날짜")
    resultMsg = models.TextField(verbose_name="결과 메세지")

    class Meta:
        verbose_name = verbose_name_plural = 'FCM 히스토리'
