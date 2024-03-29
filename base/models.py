from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # Participants = models
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.name
    
# creating one to many relationship
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.body[0:50]