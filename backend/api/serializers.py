from django.db.models import fields
from rest_framework import serializers
from .models import Riddle, Comment


class CommentSerializers(serializers.ModelSerializer):
    def get_username(self, obj):
        return {
            "username": obj.user.username
        }

    user = serializers.SerializerMethodField("get_username")

    class Meta:
        model = Comment
        fields = ['id','user','post','text','likes','dislikes','jcreated','updated']


class RiddleSerializers(serializers.ModelSerializer):
    def get_comments(self, obj):
        comments = obj.comments.all()
        serializer = CommentSerializers(comments, many=True, context=self.context)
        return serializer.data

    comments = serializers.SerializerMethodField(source='get_comments')

    class Meta:
        model = Riddle
        fields = ['id', 'title', 'text', 'jpublish', 'created', 'updated', 'comments']