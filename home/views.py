from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout , login

# Create your views here.

# password vyas@@123

def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')

def loginuser(request):
    if request.method == 'POST':
        # check if user has entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        #A backend authenticated the credentials
        else:
        #No backend authenticated the 
            return render(request, 'login.html')
    return render(request, 'login.html')


def logoutuser(request):
    logout(request)
    return redirect('/login')