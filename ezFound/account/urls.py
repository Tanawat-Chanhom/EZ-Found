"""ezFound URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from account import views
import api.views as api
import api.taggy as taggy

urlpatterns = [
    path('profile', api.userPost, name="profile"),
    path('profile/<int:userId>', api.userPost, name="profile2"),
    path('profile/edit_profile/<int:userId>', taggy.edit_profile),
    path('profile/change_password/<int:userId>', taggy.change_password),
]
