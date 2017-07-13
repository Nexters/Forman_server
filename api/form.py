from django import forms
from django.forms import ModelForm, TextInput, NumberInput, BooleanField
from suit.widgets import AutosizedTextarea, SuitSplitDateTimeWidget, LinkedSelect, EnclosedInput, SuitDateWidget

from .models import ApiToken


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

