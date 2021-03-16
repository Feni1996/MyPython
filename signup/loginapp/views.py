from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'loginapp/success.html', {'user': request.user})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return redirect('/loginapp/success')
    else:
        form = AuthenticationForm()

    return render(request, 'loginapp/login.html', {'login': form})

