from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, logout, login as auth_login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect

from restaurant_app.models import Restaurant
from .forms import UserForm
from .models import MyUser


def login(request):
    if request.method == 'POST':
        user = authenticate(phone_number=request.POST.get('phone_number'),
                            password=request.POST.get('password'))
        if user:
            auth_login(request, user)
            # set user-specific data in the session
            if user.is_superuser:
                return redirect('home_admin', )
            return redirect('home', )
        else:
            return HttpResponse("Invalid user")
    return render(request, "login.html")


def signin(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        # user = CustomUsers.objects.create_user(first_name=first_name, last_name=last_name, username=phone_number,
        #                                 password=password)
        # user.save()
        user = MyUser(phone_number=phone_number, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return render(request, 'home.html')
    else:
        return render(request, 'signin.html')


def signin_restaurant(request):
    if request.method == 'POSt':
        name = request.POST["name"]
        username = request.POST["username"]
        type = request.POST["type"]
        phone_number = request.POST['phone_number']
        password = request.POST["password"]
        res_user = Restaurant(name=name, username=username, type=type, phone_number=phone_number, password=password)
        res_user.save()
        return render(request, 'home.htmml')
    else:
        return render(request, 'signin_restaurant.html')


def login_restaurant(request):
    if request.method == "POST":
        phone_number = request.POST["phone_number"]
        res_password = request.POST['password']
        res_user = Restaurant.objects.filter(phone_number=phone_number).values()
        if res_user.password == res_password:
            return render(request, 'home.html')
        else:
            return HttpResponse("Invalid user")
    else:
        return render(request, 'login_restaurant')
