from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(label="username",max_length=10)
    email_id = forms.EmailField(label="email",max_length=15)
    password = forms.CharField(max_length=8, widget=forms.PasswordInput)

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']