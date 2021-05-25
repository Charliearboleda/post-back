from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import CommentSerializer
from .models import Comment

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all().order_by('id')
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all().order_by('id')
    serializer_class = CommentSerializer
