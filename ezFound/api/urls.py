from django.urls import path
import api.views as api
import api.taggy as taggy

urlpatterns = [
    path('post', api.post),                                     # Get post for index page and create new post
    path('post/<int:postId>', api.post_get),                    # Get specific post and all commmets of that post, Delete Post, Edit Post
    path('post/user/<int:userId>', api.userPost),               # Get all post of specific user
    path('post/location/<int:locationId>', api.get_location),   # Get all post in requested location
    path('post/category/<int:categoryId>', api.get_category),   # Get all post in requested category
    path('post/status/<str:status>', api.get_status),           # Get all post in requested status
    path('profile/<int:userId>', api.profile),                  # Get profile of user
    path('comment', api.comment),                               # Post, edit comments
    path('comment/<int:commentId>', api.del_comment),           # Delete comments
    path('message/<int:id>', api.get_message),                  # Get, Delete message of a user (Send user_id if want a message of a user, Send id of message if want to delete message)
    path('suggest/<int:userId>', api.suggest),
    path('change_password/<int:userId>', taggy.change_password),
    path('edit_profile/<int:userId>', taggy.edit_profile),
    path('forget_password', taggy.forget_password),
    path('reset_password', taggy.reset_password),
]