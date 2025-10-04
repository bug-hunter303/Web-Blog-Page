
from django.contrib import admin
from django.urls import include , path
from users import views

urlpatterns = [
    path('',views.register, name='register'),
]