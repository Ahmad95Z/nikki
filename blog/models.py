from django.utils import timezone
from django.conf import settings
from django.db import models 
from .models import User

class Post(models.Model):
    title= models.CharField(max_length=140)
    text = models.TextField(max_length=500)
    create_at = models.DateTimeField(blank=True, null= True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def create(self):
        self.create_at = timezone.now()
        self.save()

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True) 
    status = models.BooleanField(verbose_name='комментарии')
    create_at = models.DateTimeField(auto_now=True)
    comm = models.CharField(max_length=320)