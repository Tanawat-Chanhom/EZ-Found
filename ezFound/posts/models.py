from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    delete_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Location(models.Model):

    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    delete_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Post(models.Model):

    LOST = "lost"
    FOUND = "found"
    RETURNED = "returned"
    STATUS_OF_ITEM = [
        (LOST, "Lost"),
        (FOUND, "Found"),
        (RETURNED, "Returned")
    ]

    title = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True) 
    status = models.CharField(
        max_length=10, 
        choices=STATUS_OF_ITEM
    )

    date = models.DateTimeField(auto_now_add=True)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE) # Whose post
    location_id = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL) # Where're it lost

    category_id = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    
class Comment(models.Model):

    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True) 
    delete_at = models.DateTimeField(null=True, blank=True)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)

class PostImage(models.Model):

    image_id = models.IntegerField()
    image_url = models.TextField()
    delete_at = models.DateTimeField(null=True, blank=True)
    post_id = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)