from django.urls import path, include
from .views import RiddleViewSet, CommentViewSet
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()
router.register('riddle', RiddleViewSet, basename = 'riddle')
router.register('comment', CommentViewSet, basename = 'comment')

urlpatterns = [
    path('', include(router.urls)),
]