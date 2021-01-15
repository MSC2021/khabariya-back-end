from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title',]

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = NewsArticle
        fields = ['title','category','youtube_link','images','paragraph']
        lookup_field = 'title'