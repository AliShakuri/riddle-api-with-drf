from rest_framework import serializers
from .models import Riddles

class RiddleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Riddles
        fields = "__all__"
