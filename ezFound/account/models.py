from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    student_id = models.CharField(max_length=8)
    phone = models.CharField(max_length=10)
    information = models.TextField()
    profile_img_path = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

