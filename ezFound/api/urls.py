from django.urls import path
import api.views as api

urlpatterns = [
    path('post', api.post),                                     # Get post for index page and create new post
    path('post/<int:postId>', api.post_get),                    # Get specific post
    path('post/user/<int:userId>', api.userPost),               # Get all post of specific user
    path('post/location/<int:locationId>', api.get_location),   # Get all post in requested location
    path('post/category/<int:categoryId>', api.get_category),   # Get all post in requested caategory
    path('profile/<int:userId>', api.profile),                  # Get profile of user
    path('comment', api.comment),                               # Post, edit comments
    path('comment/<int:commentId>', api.del_comment),           # Delete comments
]