# ---------- Django Import ----------

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# ---------- Library Import ----------

from json import loads

# ---------- Module Import ----------

from account.models import Profile



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
        user = User.objects.create_user(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            email=request.POST.get('email'),
            first_name=request.POST.get('fname'),
            last_name=request.POST.get('lname')
        )
        profile = Profile(
            student_id=request.POST.get('student_id'),
            phone=request.POST.get('phone'),
            information=request.POST.get('information'),
            profile_img_path=request.POST.get('profile_img_path'),
            user=user
        )
        user.save()
        profile.save()
        return HttpResponse('User Created', status=201)

    else:
        return HttpResponseNotAllowed("Method Not Allow", status=405)


@require_http_methods(["GET", "POST"])
def signIn(request):

    if request.method == 'GET':
        return render(request, 'authen/signIn.html')

    elif request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'), 
            password=request.POST.get('password')
        )

        if user is not None:
            login(request, user)
            return HttpResponse('Login Success', status=200)

        else:
            return HttpResponseBadRequest('Incorrect Username Or Password', status=400)

    else:
        return HttpResponseNotAllowed("Method Not Allow", status=405)