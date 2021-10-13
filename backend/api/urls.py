from django.urls import path, include
from .views import RiddleViewSet
from rest_framework import routers

app_name = 'api'

router = routers.SimpleRouter()
router.register('riddle', RiddleViewSet, basename = 'riddle')

urlpatterns = [
    path('', include(router.urls)),
]