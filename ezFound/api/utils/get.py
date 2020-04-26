""" This module's purpose is for getting all the shit done so I don't have to write long ass code """

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from posts.models import Post, Comment
from account.models import Profile


def user(id):
    try:
        user = User.objects.get(pk=id)
        profile = Profile.objects.get(user_id=id)
        data = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "profile_img": profile.profile_img_path
        }
        return data
    
    except ObjectDoesNotExist:
        return None


def comment(id):
    comments = Comment.objects.filter(post_id=id)
    payload = [{
        "id": c.id,
        "text": c.text,
        "create_at": c.create_at,
        "delete_at": c.delete_at,
        "user": user(c.user_id)
    } for c in comments]

    return payload
