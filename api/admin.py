from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, StackedInline
from .models import Api, ApiHeader, ApiToken, ApiService, ApiServiceParams, ApiParams
from .form import ApiTokenForm, ApiParamsForm, ApiHeaderForm, ApiAdminForm, ApiServiceParamsForm, ApiServiceAdminForm

# Register your models here.
class ApiHeaderInlines(TabularInline):
    model = ApiHeader
    form = ApiHeaderForm
    extra = 0
    verbose_name_plural = 'API 헤더'
    suit_classes = 'suit-tab suit-tab-header'


class ApiTokenInlines(StackedInline):
    model = ApiToken
    form = ApiTokenForm
    extra = 0
    verbose_name_plural = 'API 토큰'
    suit_classes = 'suit-tab suit-tab-token'

class ApiPramsInlines(TabularInline):
    model = ApiParams
    form = ApiParamsForm
    extra = 0
    verbose_name_plural = 'API 파라미터'
    suit_classes = 'suit-tab suit-tab-params'

class ApiServiceInlines(StackedInline):
    model = ApiService
    form = ApiServiceAdminForm
    extra = 0
    verbose_name_plural = 'API 서비스'
    suit_classes = 'suit-tab suit-tab-services'

class ApiAdmin(ModelAdmin):
    fieldsets = ((None, {
        'classes': ('suit-tab suit-tab-general',),
        'fields': ('name', 'desc', 'type', 'useYN',)
    }),)
    list_display = ('name', 'desc', 'type', 'useYN',)
    suit_form_tabs = (('general', '일반'), ('header', '헤더'), ('token', '토큰'), ('params', '파라미터'),('services', '서비스'))
    inlines = [ApiHeaderInlines, ApiTokenInlines, ApiPramsInlines, ApiServiceInlines]
    form = ApiAdminForm


admin.site.register(Api, ApiAdmin)

class ApiServicePramsInlines(TabularInline):
    model = ApiServiceParams
    form = ApiServiceParamsForm
    extra = 0
    verbose_name_plural = 'API 파라미터'
    suit_classes = 'suit-tab suit-tab-params'

class ApiServiceAdmin(ModelAdmin):
    fieldsets = ((None, {
        'classes': ('suit-tab suit-tab-general',),
        'fields': ('name', 'desc', 'reqUrl', 'resType', 'useYN',)
    }),)
    list_display = ('get_api_desc', 'desc', 'name', 'resType', 'useYN',)
    list_filter = ('api', )
    list_display_links = ('name', 'get_api_desc', 'desc', )
    suit_form_tabs = (('general', '일반'), ('params', '파라미터'))
    inlines = [ApiServicePramsInlines, ]
    form = ApiServiceAdminForm

    def get_api_desc(self, obj):
        return obj.api.desc

    get_api_desc.short_description = 'API명'

admin.site.register(ApiService, ApiServiceAdmin)
