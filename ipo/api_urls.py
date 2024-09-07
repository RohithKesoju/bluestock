# api_urls.py
from django.urls import path
from .views import IPOListCreateView, IPODetailView

urlpatterns = [
    path('ipos/', IPOListCreateView.as_view(), name='ipo-list'),
    path('ipos/<int:pk>/', IPODetailView.as_view(), name='ipo-detail'),
]
