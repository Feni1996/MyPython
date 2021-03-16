from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import LoginForm,SignupForm
from django.contrib.auth import authenticate,login
from django.contrib import messages

def login_view(request,template_name='login.html'):
    form = LoginForm(request.POST or None)
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect("logged_in")
        else:
            messages.info(request,"either the username or password is wrong")
    return render(request,template_name,{'form':form})

def logged_in(request):
    return render(request,'success.html')

def sign_up(request,template_name='signup.html'):
    form1 = SignupForm(request.POST or None)
    if form1.is_valid():
        form1.save()
        messages.success(request,"user created")

        return redirect("login_page")
    return render(request,template_name,{'form1':form1})
