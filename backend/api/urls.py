from django.urls import path, include
from .views import RiddleViewSet, CommentViewSet
from rest_framework import routers
from .views import like, dislike

app_name = 'api'

router = routers.SimpleRouter()
router.register('riddle', RiddleViewSet, basename = 'riddle')
router.register('comment', CommentViewSet, basename = 'comment')

urlpatterns = [
    path('', include(router.urls)),
    path('comment/<int:pk>/like', like, name='like'),
    path('comment/<int:pk>/dislike', dislike, name='dislike'),
]