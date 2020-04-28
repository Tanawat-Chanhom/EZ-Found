from django.shortcuts import render, redirect
from django.views import View
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils.timezone import now
from email.message import EmailMessage

from posts.models import Post, Comment, Message, Location, Category, PostImage
from authen.models import OTP
from account.models import Profile
from api.utils.get import comment as getComment
from api.utils.get import image as getImage
from django.contrib.auth import authenticate, logout
from django.db.models import Q

import smtplib
import random
import string
from datetime import timedelta

"""
    TODO: All Done!...For Now (Add Task Here)
"""

@api_view(['PUT'])
def change_password(request, userId):
    """ Change User Password """
    if request.method == 'PUT':
        try:
            user = User.objects.get(pk=userId)
            data = {
                "username": request.data['username'],
                "old_password": request.data['old_password'],
                "password": request.data['new_password'],
                "an_password": request.data['confirm_password']
            }
            user = authenticate(
                request,
                username = request.data['username'],
                password = request.data['old_password']
            )
            if user is not None:
                if data['password'] == data['an_password']:
                    user.set_password(data['password'])
                    user.save()
                    logout(request)
                    return JsonResponse({
                        "statusCode": 200,
                        "statusText": "Success",
                        "message": "Password Changed!",
                        "error": False
                    })
            else:
                return JsonResponse({
                    "statusCode": 400,
                    "statusText": "Bad Request",
                    "message": "Password and Confirm Password mismatch.....",
                    "error": True
                })
        except ObjectDoesNotExist:
            return JsonResponse({
                "statusCode": 404,
                "statusText": "Not Found",
                "message": "User Not Exist",
                "error": True
            })


@api_view(['PUT'])
def edit_profile(request, userId):
    """ Edit Profile of User """
    try:
        try:
            user = User.objects.get(pk=userId)
            profile = Profile.objects.get(user_id=userId)
            user.first_name = request.data['first_name'] if 'first_name' in request.data else user.first_name
            user.last_name = request.data['last_name'] if 'last_name' in request.data else user.last_name
            user.email = request.data['email'] if 'email' in request.data else user.email
            profile.phone = request.data['phone'] if 'phone' in request.data else profile.phone
            profile.profile_img_path = request.data['profile_img_path'] if 'profile_img_path' in request.data else profile.profile_img_path
            profile.information = request.data['information'] if 'information' in request.data else profile.information
            user.save()
            profile.save()
            return JsonResponse({
                    "statusCode": 200,
                    "statusText": "Success",
                    "message": "Save profile success",
                    "error": False
                })

        except ObjectDoesNotExist:
            return JsonResponse({
                "statusCode": 404,
                "statusText": "Not Found",
                "message": "User Not Exist",
                "error": True
            })
    except:
        return JsonResponse({
            "statusCode": 500,
            "statusText": "Internal Server",
            "message": "Internal Server",
            "error": True
        })

@api_view(['POST'])
def forget_password(request):
    """ User Forget Password """
    if request.method == 'POST':
        try:
            specific_user = User.objects.get(email=request.POST.get('email'))
            if specific_user is not None:
                otp_code = randomString()
                ref_code = randomString()
                del_at = now() + timedelta(minutes=5)
                otp = OTP(ref_code=ref_code, otp_code=otp_code, expire_at=del_at, user=specific_user)
                otp.save()
                username = "mrkstyut@gmail.com"
                password = "4D47D0FA"
                receivers = specific_user.email
                msg = EmailMessage()
                msg.set_content(f'This is your OTP code: {otp_code}')
                msg['Subject'] = 'OTP Code'
                msg['From'] = username
                msg['To'] = receivers
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(username ,password)
                server.send_message(msg)
                server.quit()
                return render(request, 'authen/resetPass.html', context={
                    'ref_code': ref_code
                })
        except:
            return render(request, 'authen/forgotPass.html', context={
                'error': "User with that email doesn't Existed"
            })
            # return JsonResponse({
            #     "statusCode": 404,
            #     "statusText": "Not Found",
            #     "message": "User with that email doesn't Existed",
            #     "error": True
            # })

@api_view(['POST'])
def reset_password(request):
    """ Reset Password """
    if request.method == 'POST':
        try:
            data = {
                "ref_code": request.POST.get('ref_code'),
                "otp_code": request.POST.get('otp_code'),
                "new_password": request.POST.get('new_password'),
                "confirm_password": request.POST.get('confirm_password')
            }
            otp_obj = OTP.objects.get(Q(otp_code=data['otp_code']), Q(ref_code=data['ref_code']))
            if otp_obj is not None:
                user = User.objects.get(id=otp_obj.user_id)
                if data['new_password'] == data['confirm_password']:
                    user.set_password(data['new_password'])
                    user.save()
                    logout(request)
                    # return JsonResponse({
                    #     "statusCode": 200,
                    #     "statusText": "Success",
                    #     "message": "Password Changed!",
                    #     "error": False
                    # })

                    return redirect('signIn')
                else:
                    return render(request, 'authen/resetPass.html', context={
                        'ref_code': request.POST.get('ref_code'),
                        'error': "Password and Confirm Password mismatch....."
                    })
                    # return JsonResponse({
                    #     "statusCode": 400,
                    #     "statusText": "Bad Request",
                    #     "message": "Password and Confirm Password mismatch.....",
                    #     "error": True
                    # })
        except:
            return render(request, 'authen/resetPass.html', context={
                'ref_code': request.POST.get('ref_code'),
                'error': "Cannot found specific user"
            })
            # return JsonResponse({
            #     "statusCode": 404,
            #     "statusText": "Not Found",
            #     "message": "Cannot found specific user",
            #     "error": True
            # })

def randomString(stringLength=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))