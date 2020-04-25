from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=False, null=True, default=None)
    def __str__(self):
        return self.name
    


class Location(models.Model):

    name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=False, null=True, default=None)
    def __str__(self):
        return self.name


class Post(models.Model):

    POST_STATUS = [
        ('LOST', 'LOST'),
        ('FOUND', 'FOUND'),
        ('RETURNED', 'RETURNED')
    ]

    title = models.CharField(max_length=255)
    descriptions = models.TextField(default=None)
    status = models.CharField(
        max_length=8,
        choices=POST_STATUS
    )
    date = models.DateField(auto_now=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=False, null=True, default=None)
    def __str__(self):
        return '%s' % (self.title)


class PostImage(models.Model):

    image_url = models.TextField(default=None)
    create_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=False, null=True, default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Message(models.Model):

    text = models.TextField()
    is_seen = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=False, null=True, default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    send_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="send_by")
    message_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_to")
    def __str__(self):
        return '(%s) %s' % (self.user, self.create_at)


class Comment(models.Model):

    text = models.TextField()
    create_at = models.DateTimeField(auto_now=True)
    delete_at = models.DateTimeField(auto_now=False, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return '(%s) %s' % (self.user, self.create_at)