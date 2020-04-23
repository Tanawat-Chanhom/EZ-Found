from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=False, default=None)


class Location(models.Model):

    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=False, default=None)


class Post(models.Model):

    POST_STATUS = [
        ('LOST', 'LOST'),
        ('FOUND', 'FOUND'),
        ('RETURNED', 'RETURNED')
    ]

    title = models.CharField(max_length=255)
    descriptions = models.TextField()
    status = models.CharField(
        max_length=8,
        choices=POST_STATUS
    )
    date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)


class PostImage(models.Model):

    image_url = models.TextField()
    create_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=False, default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Message(models.Model):

    text = models.TextField()
    is_seen = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    send_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_by")
    message_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_to")


class Comment(models.Model):

    text = models.TextField()
    create_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=False, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)