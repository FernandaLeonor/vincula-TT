from django import forms
from apps.application_user.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Email"