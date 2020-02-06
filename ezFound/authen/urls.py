from django.contrib import admin
from django.urls import path, include
from authen import views

urlpatterns = [
    path('/login/<slug:username>/<slug:password>', views.login)
]