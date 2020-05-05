from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('lab1/', include("lab1.urls")),
    path('lab2/', include('lab2.urls')),
    path('lab3/', include('lab3.urls')),
]
