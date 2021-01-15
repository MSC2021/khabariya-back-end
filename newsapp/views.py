from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class NewsAppViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = NewsArticle.objects.all()
        category = self.request.query_params.get('category', None)
        search_value = self.request.query_params.get('search', None)
        if category is not None:
            queryset = queryset.filter(category__title=category)
        if search_value is not None:
            queryset = queryset.filter(title__icontains=search_value)
        return queryset