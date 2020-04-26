from django.shortcuts import render
from django.views import View
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from posts.models import Post, Comment, Message, Location, Category, PostImage
from authen.models import OTP
from account.models import Profile

# Create your views here.


@api_view(['GET'])
def post_get(request, postId):
    """ Get Specific Post """

    try:
        post = Post.objects.get(pk=postId)
        return JsonResponse({
            "statusCode": 200,
            "statusText": "Success",
            "message": "Successt",
            "error": False,
            "data": {
                "id": postId,
                "title": post.title,
                "description": post.descriptions,
                "status": post.status,
                "location": post.location.name,
                "user": post.user.username,
                "create_at": post.create_at,
                "date": post.date
            }
        })
    except ObjectDoesNotExist:
        return JsonResponse({
            "statusCode": 404,
            "statusText": "Not Found",
            "message": "Post Not Exist",
            "error": True
        })


@api_view(['GET'])
def userPost(request, userId):
    """ Get all post of specific user """

    try:
        post = Post.objects.filter(user_id=userId)
        payload = [{
            "id": p.id,
            "title": p.title,
            "description": p.descriptions,
            "status": p.status,
            "location": p.location.name,
            "user": p.user.username,
            "create_at": p.create_at,
            "date": p.date
        } for p in post]

        return JsonResponse({
            "statusCode": 200,
            "statusText": "Success",
            "message": "Successt",
            "error": False,
            "data": payload
        })
    except ObjectDoesNotExist:
        return JsonResponse({
            "statusCode": 404,
            "statusText": "Not Found",
            "message": "Post Not Exist",
            "error": True
        })


@api_view(['GET', 'POST'])
def post(request):
    """ Get Post For Index Page """