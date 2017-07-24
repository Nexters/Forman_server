from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Fcm
from .models import FcmMessageHistory

class FcmAdmin(ModelAdmin):
    list_display = ('user', 'token', 'useYN', 'createdDate',)

admin.site.register(Fcm, FcmAdmin)

class FcmMessageHistoryAdmin(ModelAdmin):
    list_display = ('id', 'receiver', 'sentData', 'sentDate', 'resultCode', 'resultMsg', )

    # def has_add_permission(self, request):
    #     return False

admin.site.register(FcmMessageHistory, FcmMessageHistoryAdmin)