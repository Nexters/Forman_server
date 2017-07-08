from django.db import models
from django.utils import timezone

# Create your models here.
class Apiconfig(models.Model):
    api_type = (
        (0, 'Dev'),
        (1, 'Real'),
    )
    name = models.TextField(max_length=100, verbose_name='이름')
    type = models.IntegerField(choices=api_type, verbose_name='종류')
    token = models.TextField(max_length=500, verbose_name='토큰')
    remark = models.TextField(null=True, blank=True, verbose_name='기타')
    expiredDate = models.DateField(null=True, blank=True, verbose_name='만료일')
    createdDate = models.DateTimeField(default=timezone.now, verbose_name='등록일')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = 'API 설정'

