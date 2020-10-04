from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog')
    blog_text=models.CharField(max_length=200)
    def __str__(self):
        return self.blog_text