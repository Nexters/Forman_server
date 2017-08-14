from django import forms
from django.forms import ModelForm, SelectMultiple, TextInput

from .models import GroupUsers


class GroupUsersForm(ModelForm):
    class Meta:
        model = GroupUsers
        fields = ('user', 'type', )
        widgets = {
            'user': TextInput,
            'type': TextInput,
        }


class GroupAdminForm(ModelForm):
    class Meta:
        widgets = {
            'name': TextInput,
            'type': SelectMultiple(attrs={'style': 'width:80px;',}),
            'link': TextInput,
        }