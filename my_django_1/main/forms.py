from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# class UserLoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Ввудите имя полльзователя'}))
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
#
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#
#
# class UserRegistrationForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Ввудите имя полльзователя'}))
#
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль1'}))
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите пароль2'}))
#
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2')\




from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')

