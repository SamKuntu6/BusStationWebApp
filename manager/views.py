from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user


@unauthenticated_user
def homepage(request):
    context = {}
    return render(request, 'manager/userpage.html', context)


@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='manager')
            user.groups.add(group)
            email = user.email
            name = user.first_name + " " + user.last_name
            show_name = name.__str__()

            Manager.objects.create(
                user=user,
                name=show_name,
                email=email
            )
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login_page')
    context = {'form': form}

    context = {}
    return render(request, 'manager/register.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'manager/login.html', context)


@login_required(login_url='login_page')
def manager_homepage(request):
    context = {}
    return render(request, 'manager/index.html', context)


@login_required(login_url='login_page')
def revenue_page(request):
    context = {}
    return render(request, 'manager/revenue.html', context)


@login_required(login_url='login_page')
def stand_data(request):
    context = {}
    return render(request, 'manager/viewbusstand.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')