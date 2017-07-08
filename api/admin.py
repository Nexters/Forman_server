from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput, DateInput
from .models import Apiconfig

# Register your models here.
class ApiConfigAdminForm(ModelForm):
    class Meta:
        widgets = {
            'name': TextInput,
            'token': TextInput,
            'remark': TextInput,
            'createdDate': DateTimeInput
        }

class ApiConfigAdmin(ModelAdmin):
    search_fields = ('name', 'token', 'remark',)
    list_filter = ('type',)
    list_display = ('name', 'type', 'token', 'remark', 'expiredDate', 'createdDate')
    readonly_fields = ['createdDate', ]
    date_hierarchy = 'expiredDate'
    form = ApiConfigAdminForm

admin.site.register(Apiconfig, ApiConfigAdmin)
