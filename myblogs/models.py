from django.db import models
from django.utils import timezone

class User_messages(models.Model):
    name = models.CharField(max_length=50)
    qq= models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    register_date = models.DateTimeField(default=timezone.now)
    
        
    def __str__(self):
        return self.name
class Post_messages(models.Model):
    username = models.ForeignKey(User_messages)
    title = models.CharField(max_length=200)
    slug= models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
     
    class Meta:
        ordering = ('-pub_date',)
        
    def __str__(self):
        return self.title
