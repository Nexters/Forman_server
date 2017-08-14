from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline, TabularInline

from .models import Group, GroupUsers, Schedule, Routine
from .form import GroupUsersForm, GroupAdminForm


class GroupUsersInlines(TabularInline):
    model = GroupUsers
    form = GroupUsersForm
    extra = 0
    verbose_name_plural = '그룹원'
    suit_classes = 'suit-tab suit-tab-groupusers'


class GroupAdmin(ModelAdmin):
    fieldsets = ((None, {
        'classes': ('suit-tab suit-tab-general', ),
        'fields': ('name', 'type', 'link', )
    }),)
    list_display = ('name', 'type', 'link',)
    suit_form_tabs = (('general', '일반'), ('groupusers', '그룹원'))
    inlines = [GroupUsersInlines]
    form = GroupAdminForm


admin.site.register(Group, GroupAdmin)
