from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from . managers import Mymanager
User = get_user_model

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    #the user custom manager
    
    objects = Mymanager()


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
    User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    rules = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]


class Follow(models.Model):  #consider using profile as a model
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, unique=False)
    follower = models.ManyToManyField(User, blank= True, related_name='my_follower')
    following = models.ManyToManyField(User, related_name='is_following')

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def follow_receiver_func(sender, instance, *args, **kwargs):
    follow = Follow.objects.get_or_create(user=instance)


    # objects = Mymanager()


class Liking(models.Model): 
    user = models.ManyToManyField(User)
    like = models.ManyToManyField(User, related_name='user_likes', blank=True)
    unlike = models.ManyToManyField(User, related_name='user_unlikes', blank=True)
    room = models.ManyToManyField(Room)

    def __str__(self):
        return self.user.username