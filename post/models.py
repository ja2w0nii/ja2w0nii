from django.db import models
from user.models import UserModel

class PostModel(models.Model):

    class Meta:
        db_table = "post"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="post")
    image = models.ImageField(upload_to="post_pics")
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content