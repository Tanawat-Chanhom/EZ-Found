from django.shortcuts import render
from django.views import View
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.utils.timezone import now

from posts.models import Post, Comment, Message, Location, Category, PostImage
from authen.models import OTP
from account.models import Profile
from api.utils.get import comment as getComment
from api.utils.get import image as getImage

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
                "password": request.data['new_password'],
                "an_password": request.data['confirm_password']
            }
            if data['password'] == data['an_password']:
                user.set_password(data['password'])
                user.save()
                return JsonResponse({
                    "statusCode": 200,
                    "statusText": "Success",
                    "message": "Post Edited!",
                    "error": False
                })
            else:
                return JsonResponse({
                    "statusCode": 400,
                    "statusText": "Bad Request",
                    "message": "Password and Confirm Password do not match",
                    "error": True
                })
        except ObjectDoesNotExist:
            return JsonResponse({
                "statusCode": 404,
                "statusText": "Not Found",
                "message": "Post Not Exist",
                "error": True
            })


@api_view(['PUT'])
def edit_profile(request, userId):
    """ Edit Profile of User """
    try:
        try:
            user = User.objects.get(pk=userId)
            profile = Profile.objects.get(user_id=userId)
            # user.username = request.data['username'] if 'username' in request.data else user.username
            user.first_name = request.data['first_name'] if 'first_name' in request.data else user.first_name
            user.last_name = request.data['last_name'] if 'last_name' in request.data else user.last_name
            user.email = request.data['email'] if 'email' in request.data else user.email
            profile.phone = request.data['phone'] if 'phone' in request.data else profile.phone
            profile.profile_img_path = request.data['profile_img_path'] if 'profile_img_path' in request.data else profile.profile_img_path
            user.save()
            profile.save()
            return JsonResponse({
                    "statusCode": 200,
                    "statusText": "Success",
                    "message": "Post Edited!",
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