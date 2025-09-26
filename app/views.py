from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app.models import Product


def page(request):
    return render(request, 'page.html')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'login.html')

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']


    # username -
    # password -

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, 'You are now logged in.')
        return redirect('/index/')
    else:
        messages.error(request, 'Invalid username or password.')
        return redirect('/login/')

def register_page(request):
    return render(request, 'regis.html')


def register_user(request):
    username = request.POST['username']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    if password != confirm_password:
        messages.error(request, "Password and Confirm password do not match!")
        return render(request, 'regis.html')

    user = User.objects.create_user(username=username, password=password)

    messages.success(request, "User created successfully!")
    messages.info(request, "User needs to verify the account!")
    return redirect('/index/')

@login_required
def foto(request):
    p = Product.objects.all() # Select * From Employee
    return render(request, 'foto.html', {"product": p})
def search(request):
    return render(request, 'search.html')
def profil(request):
    return render(request, 'profil.html')

def shop(request):
    return render(request, 'shopp.html')

def fav(request):
    return render(request, 'fav.html')


def register(request):
    return None