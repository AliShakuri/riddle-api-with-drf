from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Riddle, Comment
from .serializers import RiddleSerializers, CommentSerializers

# Create your views here.
class RiddleViewSet(ModelViewSet):
    queryset = Riddle.objects.all()
    serializer_class = RiddleSerializers


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers