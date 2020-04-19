from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    student_number = models.IntegerField(null=False, unique=True)
    phone_number = models.CharField(max_length=10)

    information = models.TextField()
    profile_img_path = models.TextField()

    def __str__(self):
        return self.user.username
    