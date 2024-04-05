from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()

from . models import Topic
from . models import Liking
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