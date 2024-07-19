from django.http import JsonResponse
from .models import Comments,Title
from .serializers import CommentSerializer, TitleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET"])
def comments_list(request):
    if request.method == "GET":
        comments = Comments.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)
@api_view(["POST"])
def add_comment(request):
    if request.method == "POST":
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
