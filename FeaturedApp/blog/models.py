from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from django.conf import settings

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, )
    content = models.TextField()
    date = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=123)

    def __str__(self): #megic /dunder methods
        return self.title