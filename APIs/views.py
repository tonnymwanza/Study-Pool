from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from . permissions import RoomPermission
from . permissions import MessagePermission
from base.models import Room
from base.models import Topic
from base.models import Message
from . seriallizers import TopicSerializer
from . seriallizers import RoomSerializer
from . seriallizers import MessageSerializer
# Create your views here.

class RoomViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, RoomPermission]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class TopicViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, RoomPermission]
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, MessagePermission]
    serializer_class = MessageSerializer