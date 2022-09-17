from pyexpat import model
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms  

class PersonRegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class PersonLoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  
    class Meta:
        model = User
        fields = ['username', 'password']