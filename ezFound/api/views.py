from django.shortcuts import render
from django.views import View
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

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
                "categories": [c.name for c in post.category.all()],
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
        posts = Post.objects.filter(user_id=userId)
        payload = [{
            "id": p.id,
            "title": p.title,
            "description": p.descriptions,
            "status": p.status,
            "category": [c.name for c in p.category.all()],
            "location": p.location.name,
            "user": p.user.username,
            "create_at": p.create_at,
            "date": p.date
        } for p in posts]

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
    """ Get post for index page and create new post """

    # try:
    if request.method == 'GET':
        posts = Post.objects.all()
        payload = [{
            "id": p.id,
            "title": p.title,
            "description": p.descriptions,
            "status": p.status,
            "location": p.location.name,
            "user": p.user.username,
            "create_at": p.create_at,
            "date": p.date
        } for p in posts]

        return JsonResponse({
            "statusCode": 200,
            "statusText": "Success",
            "message": "Successt",
            "error": False,
            "data": payload
        })

    elif request.method == 'POST':
        try:
            post = Post(
                title=request.data['title'],
                descriptions=request.data['descriptions'],
                status=request.data['status'],
                date=request.data['date'],
                user=User.objects.get(pk=request.data['user_id']),
                location=Location.objects.get(pk=request.data['location_id'])
            )
            post.save()
            for c in request.data['categories_id']:
                post.category.add(Category.objects.get(pk=c))
            post.save()

            return JsonResponse({
                "statusCode": 201,
                "statusText": "Created",
                "message": "Create Post Successfully",
                "error": False,
            })

        except KeyError:
            return JsonResponse({
                "statusCode": 400,
                "statusText": "Bad Request",
                "message": "Invalid API Payload",
                "error": True
        })

    # except:
    #     return JsonResponse({
    #         "statusCode": 500,
    #         "statusText": "Internal Server",
    #         "message": "Internal Server",
    #         "error": True
    #     })