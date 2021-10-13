from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Riddles
from .serializers import RiddleSerializers

# Create your views here.
class RiddleViewSet(ModelViewSet):
    queryset = Riddles.objects.all()
    serializer_class = RiddleSerializers