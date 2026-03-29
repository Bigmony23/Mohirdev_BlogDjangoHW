from django.db import models

from users.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/')
    category=models.CharField(max_length=200)
    tegs=models.CharField(max_length=200)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='posts')
    is_active=models.BooleanField(default=False)
    views=models.PositiveIntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Blog_Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='blog_comments')


# Create your models here.
