from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .decorators import unauthenticated_user
#from .decorators import allowed_users
#from django.http import HttpResponse
from .models import *
from .forms import IpoinfoForm
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages
from .models import *
from .forms import IpoinfoForm
from .forms import CustomLoginForm
from rest_framework import generics
from .models import Ipoinfo
from .serializers import IPOSerializer

from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# @login_required(login_url = 'login')
# @allowed_users(allowed_roles=['admin'])
def home(request):
    return render(request, 'dashboard.html')

# def registerPage(request):
#     form = UserCreationForm()
#     context = {'form': form}
#     return render(request, 'register.html')

#@unauthenticated_user -> can be used directly above the funtion and
# \reduces the code as the user authentication - (user.is_authenticated) is not required
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                #user = form.cleaned_data.get('username')
                #messages.success(request, 'Account was created for ' + form.cleaned_data['username'])
                user = form.save()
                login(request, user)  # Log the user in after registration
                return redirect('login')  # Redirect to a 'home' page or wherever you want

        else:
            # Initialize the form for a GET request
            form = RegisterForm()
        #         login(request, user)  # Log the user in after registration
        #         return redirect('home')  # Redirect to a 'home' page or wherever you want
        # else:
        #     form = RegisterForm()
        return render(request, 'register.html', {'form': form})

# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
#
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#     context = {}
#     return render(request, 'login.html')
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CustomLoginForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/admin/')  # Redirect to a 'home' page or wherever you want
                # else:
                #     messages.info(request, 'Username or Password is incorrect')
            else:
                form = CustomLoginForm()  # Reinitialize form with validation errors
        else:
            form = CustomLoginForm()

        return render(request, 'login.html', {'form': form})

# def logoutUser(request):
#     return redirect('login')

def custom_logout(request):
    # Log the user out
    logout(request)
    # Redirect to the login page or home page
    return redirect('login')

# @login_required(login_url='login')
# def home(request):

@login_required(login_url='login')
def ipoinfo(request):
    ipoinfo = Ipoinfo.objects.all()
    return render(request, 'ipoinfo.html', {'ipoinfo':ipoinfo})

def createOrder(request):
    form = IpoinfoForm()
    #request.POST or None
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = IpoinfoForm(request)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'order_form.html')


class IPOListCreateView(generics.ListCreateAPIView):
    queryset = Ipoinfo.objects.all()
    serializer_class = IPOSerializer

class IPODetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ipoinfo.objects.all()
    serializer_class = IPOSerializer

# views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
  # Only authenticated users can access this view
