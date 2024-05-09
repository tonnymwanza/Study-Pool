from rest_framework.routers import SimpleRouter

from . views import RoomViewSet
from . views import TopicViewSet
from . views import MessageViewSet

# my routers

router = SimpleRouter()

router.register('rooms_api', RoomViewSet, basename='rooms_api')
router.register('topics_api', TopicViewSet, basename='topics_api')
router.register('messages_api', MessageViewSet, basename='messages_api')

urlpatterns = router.urls