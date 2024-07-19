from rest_framework import serializers
from .models import Comments, Title
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields =["id", "text","author","date"]
class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ["id", "text"]