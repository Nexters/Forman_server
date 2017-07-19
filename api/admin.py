from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, StackedInline
from django.forms import ModelForm, TextInput, NumberInput, DateTimeInput, DateInput, CheckboxInput
from .models import Api, ApiHeader, ApiToken, ApiService, ApiServiceParams, ApiParams
from .form import ApiTokenForm

# Register your models here.
class ApiHeaderInlines(TabularInline):
    model = ApiHeader
    extra = 0
    verbose_name_plural = 'API 헤더'
    suit_classes = 'suit-tab suit-tab-header'


class ApiTokenInlines(StackedInline):
    model = ApiToken
    form = ApiTokenForm
    extra = 0
    verbose_name_plural = 'API 토큰'
    suit_classes = 'suit-tab suit-tab-token'


class ApiAdminForm(ModelForm):
    class Meta:
        widgets = {
            'name': TextInput,
            'desc': TextInput,
            'useYN': CheckboxInput,
        }


class ApiAdmin(ModelAdmin):
    fieldsets = ((None, {
        'classes': ('suit-tab suit-tab-general',),
        'fields': ('name', 'desc', 'useYN',)
    }),)
    suit_form_tabs = (('general', '일반'), ('header', '헤더'), ('token', '토큰'))
    inlines = [ApiHeaderInlines, ApiTokenInlines]
    form = ApiAdminForm


admin.site.register(Api, ApiAdmin)
admin.site.register(ApiParams)
admin.site.register(ApiService)
admin.site.register(ApiServiceParams)