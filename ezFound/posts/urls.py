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
from posts import views
import api.views as api

urlpatterns = [
    path('', api.post, name='index'),
    path('upload', views.uploadTest, name="upload"),
    path('post/<int:postId>', api.post_get, name="post_get"),
    path('post/edit/<int:postId>', views.post_edit, name="post_edit")
]
