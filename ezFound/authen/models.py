from django.db import models
from django.contrib.auth.models import User

class OTP(models.Model):
    ref_code = models.CharField(max_length=6)
    otp_code = models.CharField(max_length=6)
    create_at = models.DateTimeField(auto_now=True)
    expire_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


