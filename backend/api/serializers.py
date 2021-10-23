from django.db.models import fields
from rest_framework import serializers
from .models import Riddle, Comment


class CommentSerializers(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comment
        fields = ['id','user','username','post','text','likes','dislikes','jcreated','updated']


class RiddleSerializers(serializers.ModelSerializer):
    def get_comments(self, obj):
        comments = obj.comments.all()
        serializer = CommentSerializers(comments, many=True, context=self.context)
        return serializer.data

    comments = serializers.SerializerMethodField(source='get_comments')

    class Meta:
        model = Riddle
        fields = ['id', 'title', 'text', 'jpublish', 'created', 'updated', 'comments']