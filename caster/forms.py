from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(max_length=256)
    password = forms.CharField(max_length=256)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned = super().clean()
        self.user = authenticate(self.request, username=cleaned['username'], password=cleaned['password'])
        if not self.user:
            raise forms.ValidationError('Username or password was incorrect.')
        return cleaned

