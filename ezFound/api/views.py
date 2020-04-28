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
from api.utils.get import user as getUser

"""
    TODO: All Done!...For Now (Add Task Here)
"""

@api_view(['GET', 'DELETE', 'PUT'])
def post_get(request, postId):
    """ Get Specific Post """

    if request.method == 'GET':
        try:
            post = Post.objects.get(pk=postId)
            payload = {
                "id": postId,
                "title": post.title,
                "description": post.descriptions,
                "status": post.status,
                "category": [c.name for c in post.category.all()],
                "location": post.location.name,
                "user": post.user.username,
                "create_at": post.create_at,
                "date": post.date,
                "comments": getComment(postId),
                "images": getImage(postId),
                "user": getUser(post.user_id),
            }

            return render(request, 'posts/post.html', context={
                'Posts': payload
            })
        except ObjectDoesNotExist:
            return JsonResponse({
                "statusCode": 404,
                "statusText": "Not Found",
                "message": "Post Not Exist",
                "error": True
            })

    elif request.method == 'DELETE':
        try:
            post = Post.objects.get(pk=postId)
            post.delete_at = now()
            post.save()

            return JsonResponse({
                "statusCode": 200,
                "statusText": "Success",
                "message": "Post Deleted!",
                "error": False
            })

        except ObjectDoesNotExist:
            return JsonResponse({
                "statusCode": 404,
                "statusText": "Not Found",
                "message": "Post Not Exist",
                "error": True
            })

    elif request.method == 'PUT':
        try:
            post = Post.objects.get(pk=postId)
            post.title = request.data['title'] if 'title' in request.data else post.title
            post.descriptions = request.data['descriptions'] if 'descriptions' in request.data else post.descriptions
            post.status = request.data['status'] if 'status' in request.data else post.status

            post.save()

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
                "message": "Post Not Exist",
                "error": True
            })


@api_view(['GET'])
def userPost(request, userId):
    """ Get all post of specific user """

    try:
        posts = Post.objects.filter(user_id=userId)
        user = User.objects.get(pk=userId)
        payload = [{
            "id": p.id,
            "title": p.title,
            "description": p.descriptions,
            "status": p.status,
            "category": [c.name for c in p.category.all()],
            "location": p.location.name,
            "create_at": p.create_at,
            "date": p.date,
            "images": getImage(p.id),
            "user": getUser(p.user.id),
            "comments": getComment(p.id)
        } for p in posts if p.delete_at is None]

        # return JsonResponse({
        #     "statusCode": 200,
        #     "statusText": "Success",
        #     "message": "Successt",
        #     "error": False,
        #     "data": payload
        # })

        return render(request, 'account/profile.html', context={
            'Posts': payload,
            'User': user
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

    try:
        if request.method == 'GET':
            if request.user.is_authenticated:
                if request.GET.get('filter-search-by') == "Category":
                    posts = Post.objects.filter(category=request.GET.get('filter-category'))
                elif request.GET.get('filter-search-by') == "Location":
                    posts = Post.objects.filter(location=request.GET.get('filter-location'))
                elif request.GET.get('filter-search-by') == "Status":
                    posts = Post.objects.filter(status=request.GET.get('filter-status').upper())
                else:
                    posts = Post.objects.all()
                
                payload = [{
                    "id": p.id,
                    "title": p.title,
                    "description": p.descriptions,
                    "status": p.status,
                    "location": p.location.name,
                    "category": [c.name for c in p.category.all()],
                    "create_at": p.create_at,
                    "date": p.date,
                    "user": getUser(p.user.id),
                    "images": getImage(p.id),
                    "comments": getComment(p.id)
                } for p in posts]
                categoryAll = Category.objects.all()
                locationAll = Location.objects.all()


                return render(request, 'posts/index.html', context={
                    'Category': categoryAll,
                    'Locations': locationAll,
                    'Posts': payload
                })
            else:
                return render(request, 'authen/signIn.html')

        elif request.method == 'POST':
            try:
                # Create Post
                post = Post(
                    title=request.data['title'],
                    descriptions=request.data['descriptions'],
                    status=request.data['status'],
                    date=request.data['date'],
                    user=User.objects.get(pk=request.data['user_id']),
                    location=Location.objects.get(pk=request.data['location_id'])
                )
                
                # Add category to post
                post.save()
                for c in request.data['categories_id']:
                    post.category.add(Category.objects.get(pk=c))
                post.save()

                # Create PostImage
                for i in request.data['images']:
                    image = PostImage(
                        image_url=i,
                        post=post
                    )
                    image.save()

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

    except:
        return JsonResponse({
            "statusCode": 500,
            "statusText": "Internal Server",
            "message": "Internal Server",
            "error": True
        })


@api_view(['GET'])
def get_location(request, locationId):

    try:
        posts = Post.objects.filter(location=locationId)
        payload = [{
            "id": p.id,
            "title": p.title,
            "description": p.descriptions,
            "status": p.status,
            "category": [c.name for c in p.category.all()],
            "location": p.location.name,
            "user": getUser(p.user_id),
            "create_at": p.create_at,
            "date": p.date,
            "images": getImage(p.id)
        } for p in posts if p.delete_at is None]

        return JsonResponse({
            "statusCode": 200,
            "statusText": "Success",
            "message": "Query Success",
            "error": False,
            "data": payload
        })

    except:
        return JsonResponse({
            "statusCode": 500,
            "statusText": "Internal Server",
            "message": "Internal Server",
            "error": True
        })


@api_view(['GET'])
def get_category(request, categoryId):

    try:
        posts = Post.objects.filter(category=categoryId)
        payload = [{
            "id": p.id,
            "title": p.title,
            "description": p.descriptions,
            "status": p.status,
            "category": [c.name for c in p.category.all()],
            "location": p.location.name,
            "user": getUser(p.user_id),
            "create_at": p.create_at,
            "date": p.date,
            "images": getImage(p.id)
        } for p in posts if p.delete_at is None]

        return JsonResponse({
            "statusCode": 200,
            "statusText": "Success",
            "message": "Query Success",
            "error": False,
            "data": payload
        })

    except:
        return JsonResponse({
            "statusCode": 500,
            "statusText": "Internal Server",
            "message": "Internal Server",
            "error": True
        })

@api_view(['GET'])
def get_status(request, status):

    try:
        posts = Post.objects.filter(status=status.upper())
        print(posts[0].delete_at, posts[0])
        payload = [{
            "id": p.id,
            "title": p.title,
            "description": p.descriptions,
            "status": p.status,
            "category": [c.name for c in p.category.all()],
            "location": p.location.name,
            "user": getUser(p.user_id),
            "create_at": p.create_at,
            "date": p.date,
            "images": getImage(p.id)
        } for p in posts if p.delete_at is None]

        return JsonResponse({
            "statusCode": 200,
            "statusText": "Success",
            "message": "Query Success",
            "error": False,
            "data": payload
        })

    except:
        return JsonResponse({
            "statusCode": 500,
            "statusText": "Internal Server",
            "message": "Internal Server",
            "error": True
        })

@api_view(['GET'])
def profile(request, userId):
    """ Get Profile Of A User """
    try:
        try:
            user = User.objects.get(pk=userId)
            profile = Profile.objects.get(user_id=userId)
            return JsonResponse({
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "student_id": profile.student_id,
                "phone": profile.phone,
                "profile_img_path": profile.profile_img_path
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


@api_view(['POST', 'PUT'])
def comment(request):

    try:
        if request.method == 'POST':
            try:
                # Get Object
                user = User.objects.get(pk=request.data['user_id'])
                post = Post.objects.get(pk=request.data['post_id'])

                # Create Comment Object
                comment = Comment(
                    text=request.data['text'],
                    user=user,
                    post=post
                )

                # Create Message Object
                if user.id != post.user_id:
                    message = Message(
                        text=f"{user.first_name} Commented on your post.",
                        post=post,
                        send_by=user,
                        message_to=User.objects.get(pk=post.user_id)
                    )
                    message.save()

                # Save Object
                comment.save()

                # Response
                return JsonResponse({
                    "statusCode": 201,
                    "statusText": "Created",
                    "message": "Comment Posted!",
                    "error": False
                })

            except ObjectDoesNotExist:
                return JsonResponse({
                    "statusCode": 404,
                    "statusText": "Not Found",
                    "message": "Post Or User Not Exist",
                    "error": True
                })

        elif request.method == 'PUT':
            try:
                comment = Comment.objects.get(pk=request.data['comment_id'])
                comment.text = request.data['text']
                comment.save()

                return JsonResponse({
                    "statusCode": 200,
                    "statusText": "Success",
                    "message": "Success",
                    "error": False
                })

            except ObjectDoesNotExist:
                return JsonResponse({
                    "statusCode": 404,
                    "statusText": "Not Found",
                    "message": "Comment Not Exist",
                    "error": True
                })

    except:
        return JsonResponse({
            "statusCode": 500,
            "statusText": "Internal Server",
            "message": "Internal Server",
            "error": True
        })


@api_view(['DELETE'])
def del_comment(request, commentId):
    try:
        comment = Comment.objects.get(pk=commentId)
        comment.delete_at = now()
        comment.save()

        return JsonResponse({
            "statusCode": 200,
            "statusText": "Success",
            "message": "Comment Deleted!",
            "error": False
        })

    except ObjectDoesNotExist:
        return JsonResponse({
            "statusCode": 404,
            "statusText": "Not Found",
            "message": "Comment Not Exist",
            "error": True
        })

    except:
        return JsonResponse({
            "statusCode": 500,
            "statusText": "Internal Server",
            "message": "Internal Server",
            "error": True
        })


@api_view(['GET', 'DELETE'])
def get_message(request, id):

    try:
        if request.method == 'GET':
            messages = Message.objects.filter(message_to_id=id)

            payload = [{
                "text": m.text,
                "from": getUser(m.send_by_id),
                "create_at": m.create_at,
                "post": m.post_id,
                "messageId": m.id
            } for m in messages if m.delete_at is None]

            return JsonResponse({
                "statusCode": 200,
                "statusText": "Success",
                "message": "Query Success!",
                "error": False,
                "data": payload
            })

        elif request.method == 'DELETE':
            message = Message.objects.get(pk=id)
            message.delete_at = now()
            message.save()

            return JsonResponse({
                "statusCode": 200,
                "statusText": "Success",
                "message": "Message Deleted!",
                "error": False
            })

    except:
        return JsonResponse({
            "statusCode": 500,
            "statusText": "Internal Server",
            "message": "Internal Server",
            "error": True
        })
