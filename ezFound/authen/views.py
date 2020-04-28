# ---------- Django Import ----------

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# ---------- Library Import ----------

from json import loads
import json

# ---------- Module Import ----------

from account.models import Profile



def forgotPass(request):

    if request.method == 'GET':
        return render(request, 'authen/forgotPass.html')



def otp(request):

    if request.method == 'GET':
        return render(request, 'authen/otp.html')



def resetPass(request):

    if request.method == 'GET':
        return render(request, 'authen/resetPass.html')


@require_http_methods(["GET", "POST"])
def signUp(request):    

    if request.method == 'GET':
        return render(request, 'authen/signUp.html')

    elif request.method == 'POST':
        data = json.loads(request.body);
        user = User.objects.create_user(
            username=data['username'],
            password=data['password'],
            email=data['email'],
            first_name=data['fname'],
            last_name=data['lname']
        )
        profile = Profile(
            student_id=data['student_id'],
            phone=data['phone'],
            information=data['information'],
            profile_img_path=data['profile_img_path'],
            user=user
        )
        user.save()
        profile.save()
        responseData = {
                "statusCode": "201",
                "statusMessage": "Created",
                "errorMessage": "User Created"
            }
        return JsonResponse(responseData, safe=False)

    else:
        responseData = {
                "statusCode": "405",
                "statusMessage": "Method Not Allow",
                "errorMessage": "Method Not Allow"
            }
        return JsonResponse(responseData, safe=False)


@require_http_methods(["GET", "POST"])
def signIn(request):

    if request.method == 'GET':
        return render(request, 'authen/signIn.html')

    elif request.method == 'POST':
        data = json.loads(request.body);
        user = authenticate(
            request,
            username=data['username'], 
            password=data['password']
        )

        if user is not None:
            login(request, user)
            responseData = {
                "statusCode": "200",
                "statusMessage": "OK",
                "errorMessage": "Login Success"
            }
            return JsonResponse(responseData, safe=False)

        else:
            responseData = {
                "statusCode": "400",
                "statusMessage": "Bad request!",
                "errorMessage": "Incorrect Username Or Password"
            }
            return JsonResponse(responseData, safe=False)

    else:
        responseData = {
                "statusCode": "405",
                "statusMessage": "Method Not Allow",
                "errorMessage": "Method Not Allow"
            }
        return JsonResponse(responseData, safe=False)

def logout_view(request):
    logout(request)
    return render(request, 'authen/signIn.html')