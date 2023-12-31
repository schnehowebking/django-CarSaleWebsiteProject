from multiprocessing import AuthenticationError
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import *


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']



class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        

class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = '__all__'



class UserChangePasswordwithoutForm(UserPasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangePasswordwithoutForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['password1', 'password2']
        