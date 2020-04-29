from django.shortcuts import render
from pkg_resources import require
from django.http import JsonResponse
from posts.models import Post, Comment, Message, Location, Category, PostImage
from api.utils.get import comment as getComment
from api.utils.get import image as getImage
from api.utils.get import user as getUser

def post_edit(request, postId):
    post = Post.objects.get(pk=postId)
    payload = {
        "id": postId,
        "title": post.title,
        "description": post.descriptions,
        "status": post.status,
        "categories": [c.name for c in post.category.all()],
        "location": post.location.name,
        "user": post.user.username,
        "create_at": post.create_at,
        "date": post.date,
        "comments": getComment(postId),
        "images": getImage(postId),
        "user": getUser(post.user_id),
    }

    return render(request, 'posts/editPost.html', context={
        'Posts': payload
    })