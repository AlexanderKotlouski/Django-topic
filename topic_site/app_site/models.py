from django.contrib.auth.models import User
from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=255)
    count_post = models.IntegerField(default=100)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete= models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.topic}, {self.user}'