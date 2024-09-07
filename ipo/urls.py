from django.urls import path, include
from . import views
from .views import loginPage
from django.contrib.auth.views import LogoutView
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', views.home),
    path('', views.home, name='home'),
    path('login/', loginPage, name='login'),
    path('logout/', views.custom_logout, name='custom_logout'),
    #path('logout/', views.logout, name='logout'),
    path('ipoinfo/', views.ipoinfo),
    path('create_orders/', views.createOrder, name="create_orders"),
    path('registerpage/', views.registerPage, name="register"),
    path('loginpage/', views.loginPage, name="login"),

    path('api/', include('ipo.api_urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
]