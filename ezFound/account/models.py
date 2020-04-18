from django.db import models

# Create your models here.

class User(models.Model):
    
    username = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)

    student_number = models.IntegerField(null=False, unique=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)

    # phone_number = models.
    email = models.EmailField()

    information = models.TextField()
    profile_img_path = models.TextField()
