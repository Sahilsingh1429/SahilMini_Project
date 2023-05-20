from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('',login,name='login'),
    path('index/',index,name='index'),
    path('search/',search,name='search'),
    path('logout',logout,name='logout')
    
]