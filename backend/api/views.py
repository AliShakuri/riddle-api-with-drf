from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import Riddle, Comment
from .serializers import RiddleSerializers, CommentSerializers
from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes

# Create your views here.
class RiddleViewSet(ModelViewSet):
    queryset = Riddle.objects.all()
    serializer_class = RiddleSerializers


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)


@api_view(['POST'])
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated])
def like(request, pk):
    user = request.user
    comment = get_object_or_404(Comment, pk=pk)
    if user in comment.dislikes.all():
        comment.dislikes.remove(user)
        comment.likes.add(user)
    elif user in comment.likes.all():
        comment.likes.remove(user)
    else:
        comment.likes.add(user)
    return JsonResponse ({'liked': 'click ok'})


@api_view(['POST'])
@authentication_classes([TokenAuthentication,])
@permission_classes([IsAuthenticated])
def dislike(request, pk):
    user = request.user
    comment = get_object_or_404(Comment, pk=pk)
    if user in comment.likes.all():
        comment.likes.remove(user)
        comment.dislikes.add(user)
    elif user in comment.dislikes.all():
        comment.dislikes.remove(user)
    else:
        comment.dislikes.add(user)
    return JsonResponse ({'disliked': 'click ok'})