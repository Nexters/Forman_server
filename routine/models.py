from django.db import models
from django.contrib.auth.models import User


# 그룹
class Group(models.Model):
    type_name =(
        (0, '가족'),
        (1, '친구'),
        (2, '회사'),
        (3, '스타'),
        (4, '연인'),
    )
    name = models.TextField(verbose_name='그룹', max_length=30)
    type = models.SmallIntegerField(verbose_name='종류', choices=type_name)
    link = models.TextField(verbose_name='링크', max_length=400)


# 그룹 유저
class GroupUsers(models.Model):
    type_name = (
        (0, '그룹장'),
        (1, '그룹원'),
    )
    group = models.OneToOneField(Group, on_delete=models.CASCADE, verbose_name="그룹")
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = '사용자')
    type = models.SmallIntegerField(verbose_name='권한', choices=type_name)


# 일정
class Schedule(models.Model):
    object_choice = {
        (0, "Personal"),
        (1, "Business"),
    }
    type_choice = (
        (0, '편도'),
        (1, '왕복'),
    )
    realTimeLocation_choice = (
        (0, 'OFF'),
        (1, 'ON'),
    )
    group = models.ForeignKey(Group, verbose_name='그룹', on_delete=models.CASCADE)
    object = models.SmallIntegerField(verbose_name='목적', choices=object_choice)
    type = models.SmallIntegerField(verbose_name='종류', choices=type_choice)
    departure = models.TextField(verbose_name="출발지", max_length=30)
    departureTime = models.DateTimeField(verbose_name='출발 시간')
    arrival = models.TextField(verbose_name="도착지", max_length=30)
    arrivalTime = models.DateTimeField(verbose_name='도착 시간')
    realTimeLocation = models.SmallIntegerField(verbose_name="GPS", choices=realTimeLocation_choice, default=0)


# 루틴
class Routine(models.Model):
    type_choice = (
        (0, '자동차'),
        (1, '비행기'),
    )
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE)
    sequence = models.SmallIntegerField(verbose_name="순서")
    type = models.SmallIntegerField(verbose_name="종류", choices=type_choice)
    departure = models.TextField(verbose_name="출발지", max_length=100)
    departureTime = models.DateTimeField(verbose_name='출발 시간')
    arrival = models.TextField(verbose_name="도착지", max_length=100)
    arrivalTime = models.DateTimeField(verbose_name='도착 시간')
    distance = models.IntegerField(verbose_name="거리")
    flight_no = models.TextField(verbose_name="편명", null=True)