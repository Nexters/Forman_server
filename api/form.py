from django import forms
from django.forms import ModelForm, TextInput, NumberInput, BooleanField, SelectMultiple, Select, CheckboxInput
from suit.widgets import AutosizedTextarea, SuitSplitDateTimeWidget, LinkedSelect, EnclosedInput, SuitDateWidget

from .models import ApiToken, ApiParams, ApiHeader, ApiServiceParams


class ApiTokenForm(ModelForm):
    class Meta:
        model = ApiToken
        fields = ('name', 'useYN', 'isDev', 'token', 'remark', 'expiredDate', 'createdDate', )
        widgets = {
            'name': AutosizedTextarea,
            'token': AutosizedTextarea,
            'remark': AutosizedTextarea,
            'expiredDate': SuitDateWidget,
            'createdDate': SuitSplitDateTimeWidget
        }

class ApiParamsForm(ModelForm):
    class Meta:
        model = ApiParams
        fields = ('key', 'valueType', 'valueInputType', 'value', 'reqMethod', 'memo', )
        widgets = {
            'key': TextInput(attrs={'style': 'width:80px;', }),
            'value': TextInput(attrs={'style': 'width:100px;', }),
            'valueType': SelectMultiple(attrs={'style': 'width:90px'}),
            'memo': AutosizedTextarea,
            'reqMethod': SelectMultiple(attrs={'style': 'width:60ox'}),
            'valueInputType': SelectMultiple(attrs={'style': 'width:60ox'}),
        }

class ApiHeaderForm(ModelForm):
    class Meta:
        model = ApiHeader
        fields = ('key', 'valueType', 'value', 'memo')
        widgets = {
            'key': TextInput,
            'memo': TextInput,
            'value': AutosizedTextarea,
        }

class ApiAdminForm(ModelForm):
    class Meta:
        widgets = {
            'name': TextInput,
            'desc': TextInput,
            'useYN': CheckboxInput,
        }

class ApiServiceParamsForm(ModelForm):
    class Meta:
        model = ApiServiceParams
        fields = ('key', 'valueType', 'valueInputType', 'value', 'reqMethod', 'memo', )
        widgets = {
            'key': TextInput(attrs={'style': 'width:80px;', }),
            'value': TextInput(attrs={'style': 'width:100px;', }),
            'valueType': Select(attrs={'style': 'width:90px'}),
            'memo': AutosizedTextarea,
            'reqMethod': Select(attrs={'style': 'width:60ox'}),
            'valueInputType': Select(attrs={'style': 'width:60ox'}),
        }

class ApiServiceAdminForm(ModelForm):
    class Meta:
        widgets = {
            'name': TextInput,
            'desc': TextInput,
            'useYN': CheckboxInput,
        }