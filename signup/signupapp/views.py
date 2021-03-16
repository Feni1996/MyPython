from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.

def user_signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ user)
            return redirect('/loginapp/login')
    else:
        form = CreateUserForm()
    return render(request, 'signupapp/signup.html', {'signup': form})