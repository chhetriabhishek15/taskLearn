from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_title=models.TextField()
    post_body=models.TextField()
    post_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title
    