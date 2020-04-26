from django.urls import path
import api.views as api

urlpatterns = [
    path('post', api.post),                         # Get post for index page and create new post
    path('post/<int:postId>', api.post_get),        # Get specific post
    path('post/user/<int:userId>', api.userPost),   # Get all post of specific user
]