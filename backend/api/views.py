from django.shortcuts import get_object_or_404, redirect
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
    return redirect('api:cmnt', comment.pk)

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
    return redirect('api:cmnt', comment.pk)