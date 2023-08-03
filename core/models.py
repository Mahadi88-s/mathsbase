from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string

# Create your models here.
User = get_user_model()

class QuestionP1(models.Model):
    number = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    topic = models.CharField(max_length=50)
    marks = models.IntegerField(default=0)    
    img = models.ImageField(upload_to='img', default='')

    def __str__(self):
        return str(self.number)

class QuestionP2(models.Model):
    number = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    topic = models.CharField(max_length=50)
    marks = models.IntegerField(default=0)    
    img = models.ImageField(upload_to='img', default='')

    def __str__(self):
        return str(self.number)
    
class QuestionP3(models.Model):
    number = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    topic = models.CharField(max_length=50)
    marks = models.IntegerField(default=0)    
    img = models.ImageField(upload_to='img', default='')

    def __str__(self):
        return str(self.number)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    api_key = get_random_string(length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    
class Pwdlist(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username