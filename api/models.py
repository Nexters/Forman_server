from django.db import models
from django.utils import timezone

ValueType = (
    (0, '텍스트'),
    (1, '숫자'),
    (2, 'Bool'),
    (99, 'Token'),
)


# API 기본 세팅
class Api(models.Model):
    name = models.TextField(max_length=100, verbose_name='API 이름')
    desc = models.TextField(verbose_name='설명')
    useYN = models.BooleanField(default=True, verbose_name='사용여부')

    def __str__(self):
        return self.name


# API Token 아이디를 관리한다
class ApiToken(models.Model):
    api_type = (
        (True, 'Dev'),
        (False, 'Real'),
    )
    api_select = (
        (True, '사용'),
        (False, '미사용'),
    )
    api = models.ForeignKey(Api)
    useYN = models.BooleanField(choices=api_select, verbose_name='사용여부')
    name = models.TextField(max_length=100, verbose_name='이름')
    isDev = models.BooleanField(choices=api_type, verbose_name='종류', default=False)
    token = models.TextField(max_length=500, verbose_name='토큰')
    remark = models.TextField(null=True, blank=True, verbose_name='기타')
    expiredDate = models.DateField(null=True, blank=True, verbose_name='만료일')
    createdDate = models.DateTimeField(default=timezone.now, verbose_name='등록일')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = 'API 토큰'


class ApiHeader(models.Model):
    api = models.ForeignKey(Api)
    key = models.TextField(verbose_name='키')
    valueType = models.SmallIntegerField(choices=ValueType, verbose_name='값 종류')
    value = models.TextField(verbose_name='값')
    memo = models.TextField(verbose_name='메모')

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = verbose_name_plural = 'API 헤더'


class ApiService(models.Model):
    ResponseType = (
        (0, 'JSON'),
        (1, 'XML'),
    )

    RequestMethods = (
        (0, 'GET'),
        (1, 'POST'),
    )

    api = models.ForeignKey(Api)
    name = models.TextField(max_length=100, verbose_name='이름')
    desc = models.TextField(verbose_name='설명')
    useYN = models.BooleanField(default=True, verbose_name='사용 여부')
    resType = models.SmallIntegerField(choices=ResponseType, verbose_name='응답형식',
                                       help_text='응답하는 형식에 따라 데이터 변환을 해준다', default=0)
    reqMethod = models.SmallIntegerField(choices=RequestMethods, verbose_name='요청 형식', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = 'API 서비스'


class ApiServiceParams(models.Model):
    RequestMethods = (
        (0, 'GET'),
        (1, 'POST'),
    )

    ValueInputType = (
        (0, '사용자 직접 입력'),
        (1, '입력값'),
    )

    api = models.ForeignKey(ApiService)
    key = models.TextField(verbose_name='키')
    valueType = models.SmallIntegerField(choices=ValueType, verbose_name='값 종류')
    valueInputType = models.SmallIntegerField(choices=ValueInputType, verbose_name='값 입력 방식')
    value = models.TextField(verbose_name='값')
    reqMethod = models.SmallIntegerField(choices=RequestMethods, verbose_name='요청 형식', default=0)
    memo = models.TextField(verbose_name='메모')

    def __str__(self):
        return self.key

    class Meta:
        verbose_name = verbose_name_plural = 'API 서비스 파라미터'
