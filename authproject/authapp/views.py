from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm



# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.get_username()
            password = form.get_password()
            login(request, username, password)
            return redirect('home')
        else:
            form = AuthenticationForm()

    return render(request, 'login.html')

def passwordChange(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.get_username()
            password = form.get_password()
            login(request, username, password)
            return redirect('home')
        else:
            form = AuthenticationForm()

    return render(request, 'password_change.html')

def passwordChangeDone(request):
    return render(request, 'password_change_done.html')

