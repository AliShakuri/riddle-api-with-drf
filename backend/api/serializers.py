from rest_framework import serializers
from .models import Riddle, Comment

class RiddleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Riddle
        fields = "__all__"


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"