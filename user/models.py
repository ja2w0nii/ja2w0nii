from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):

    class Meta:
        db_table = "my_user"
        
    bio = models.TextField(max_length=500, blank=True)
    profile = models.ImageField(default="default_profile_pic.jpg",upload_to="profile_pics")