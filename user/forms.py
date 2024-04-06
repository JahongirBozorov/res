from django import forms
from .models import MyUser

class UserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['phone_number', 'password']
