from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('admin_index/',admin_index,name='admin_index'),
    path('view_product/',view_product,name='view_product'),
    path('update_product/',update_product,name='update_product'),
    path('delete/<int:cid>',delete,name='delete')
    
]