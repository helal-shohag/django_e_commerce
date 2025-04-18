from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required = True)
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','password1','password2']