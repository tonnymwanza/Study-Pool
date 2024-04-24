from django.contrib import admin
<<<<<<< HEAD
from .models import Room, Topic, Message, User
=======
from .models import Room
from . models import Topic
from . models import Message
from . models import User
>>>>>>> working-branch
# Register your models here.

admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)