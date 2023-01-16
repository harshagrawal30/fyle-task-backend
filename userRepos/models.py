from django.db import models
from django_mysql.models import ListCharField
# Create your models here.
class user(models.Model):
    username = models.CharField(max_length = 200,unique=True)
    name = models.CharField(max_length=200,default='')
    avatar = models.FileField(upload_to = 'avatars',blank = True)
    location = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    twitter = models.CharField(max_length=200,blank=True)
    linkedin = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.username


class repositories(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE,related_name='user_repositories')
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name +" of "+self.user.username.upper()

class languages(models.Model):
    repositories = models.ForeignKey(repositories,on_delete=models.CASCADE,related_name='repository_language')
    language = models.CharField(max_length=50)
    def __str__(self):
        return self.language + " of "+ self.repositories.name.upper() + " by " + self.repositories.user.username.upper()