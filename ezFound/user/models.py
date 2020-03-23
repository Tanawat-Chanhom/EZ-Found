from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_number = models.IntegerField()
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    phonenumber = models.IntegerField()
    email = models.EmailField(max_length=255)
    information = models.TextField()
    profile_img_path = models.TextField()