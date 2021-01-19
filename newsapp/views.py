from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import *
from .serializers import *
# Create your views here.

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'title'
    
class NewsAppViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsSerializer
    
    def get_queryset(self):
        queryset = NewsArticle.objects.filter(publish=True).order_by('-timestamp')
        category = self.request.query_params.get('category', None)
        search_value = self.request.query_params.get('search', None)
        if category is not None:
            queryset = queryset.filter(category__title=category).order_by('-timestamp')
        if search_value is not None:
            queryset = queryset.filter(title__icontains=search_value).order_by('-timestamp')
        return queryset

class VideoLinkView(generics.ListCreateAPIView):
    queryset = NewsArticle.objects.all().exclude(youtube_link=[])
    serializer_class = VideoLinkSerializer
