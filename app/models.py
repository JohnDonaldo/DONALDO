from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()



def __str__(self):
    return self.title

def get_absolute_url(self):
    return reverse('blog-detail', kwargs={'pk': self.pk})