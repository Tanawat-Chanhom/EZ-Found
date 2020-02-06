from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import request

# Create your views here.

def login(request, username, password):
    return HttpResponse("Username: %s Password: %s" %(username, password))
