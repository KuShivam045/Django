from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', insert1),
    path('employee', employee),
    path('read', view_data),
    path('update', update_),
    
]
