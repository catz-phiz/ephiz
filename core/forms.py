from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

cssForForm = 'w-full py-4 px-6 rounded-xl'

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': cssForForm,
    })) 

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': cssForForm,
    }))

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')
    

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': cssForForm,
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': cssForForm,
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': cssForForm,
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': cssForForm,
    }))