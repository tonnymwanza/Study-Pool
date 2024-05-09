from rest_framework.serializers import ModelSerializer

from base.models import Room
from base.models import Topic
from base.models import Message

# my serializers

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'host',
            'topic',
            'name',
            'description',
            'created',
            'rules',
        ]

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = [
            'name'
        ]

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = [
            'user',
            'room',
            'body',
            'created'
        ]