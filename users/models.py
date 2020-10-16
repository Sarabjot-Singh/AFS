from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default="default.png", upload_to="profile_pics")
    mobile = models.CharField(max_length=10, primary_key = True)
    balance = models.IntegerField(default=0)
    qr_code = models.ImageField(default="default1.png", upload_to="qr_codes")

    def __str__(self):
        return f'{self.user.username} Profile'

