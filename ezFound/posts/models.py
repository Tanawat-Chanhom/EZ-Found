from django.db import models
from account.models import User
from enum import Enum

class StatusPost(Enum):
    lost = "Lost"
    found = "Found"
    returned = "Returned"

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    delete_at = models.DateTimeField(auto_now=True)

class Location(models.Model):

    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    delete_at = models.DateTimeField(auto_now=True)

class Post(models.Model):

    title = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True) 
    status = models.CharField(
        max_length=10, 
        choices=[(tag, tag.value) for tag in StatusPost]
    )

    date = models.DateTimeField(auto_now_add=True)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE) # Whose post
    location_id = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL) # Where're it lost

    category_id = models.ManyToManyField(Category)
    
class Comment(models.Model):

    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True) 
    delete_at = models.DateTimeField(auto_now=True)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class PostImage(models.Model):

    image_id = models.IntegerField()
    image_url = models.TextField()
    delete_at = models.DateTimeField(auto_now=True)
    post_id = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)