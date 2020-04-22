# ---------- Django Import ----------

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User

# ---------- Library Import ----------

from json import loads

# ---------- Module Import ----------

from account.models import UserProfile

def forgotPass(request):
    return render(request, 'authen/forgotPass.html')


def otp(request):
    return render(request, 'authen/otp.html')


def resetPass(request):
    return render(request, 'authen/resetPass.html')


@require_http_methods(["GET", "POST"])
def signUp(request):
    if request.method == 'GET':
        return render(request, 'authen/signUp.html')
    elif request.method == 'POST':
        body_unicode = HttpRequest.body
        print(body_unicode)
        user = User.objects.create_user(
            username="",
            password="",
            email="",
            first_name="",
            last_name=""
        )
    else:
        return HttpResponseNotAllowed()


def signIn(request):
    return render(request, 'authen/signIn.html')