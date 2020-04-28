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

from authen import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('otp', views.otp, name="otp"),
    path('reset-pass', views.resetPass, name="resetPass"),
    path('sign-in', views.signIn, name="signIn"),
    path('sign-up', views.signUp, name="signUp"),
    path('forgot-pass', views.forgotPass, name="forgotPass"),
    path('logout', views.logout_view, name="logout")
]
