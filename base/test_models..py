from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()

from . models import Topic
from . models import Room
from . models import Message
# Create your tests here.


class TestCaseUser(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser',is_staff=True, password='123')

    def test_user(self, user):
        return self.assertEqual(self.user, 1)

class LikingTestCase(TestCase):
    pass

class TopicTestCase(TestCase):

    def setUp(self):
        topic = Topic.objects.create(name='football')

    def test_topic(self):
        topic = Topic.objects.filter(name__iexact='footbal')
        self.assertTrue(topic)


class RoomTestCase(TestCase):

    def setUp(self):
        self.room = Room.objects.create(
            name = 'the room',
            description = 'the best room available',
            updated = '2024-07-07',
            created = '2024-07-06',
            rules = 'no insults',
        )

    def test_room(self):
        self.assertEqual(self.room.name, 'the room')
        self.assertEqual(self.room.description, 'the best room available')
        self.assertEqual(self.room.updated, '2024-07-07')
        self.assertEqual(self.room.created, '2024-07-06')
        self.assertEqual(self.room.rules, 'no insults')


class MessageTestCase(TestCase):
    
    def setUp(self):
        self.message = Message.objects.create(
            body = 'this is my message',
            updated = '2024-06-23',
            created = '2024-06-15'
        )

    def test_message(self):
        self.assertEqual(self.message.body, 'this is my message')
        self.assertEqual(self.message.updated, '2024-06-23')
        self.assertEqual(self.message.created, '2024-06-15')