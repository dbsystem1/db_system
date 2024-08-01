from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label='Password', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
     
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
  