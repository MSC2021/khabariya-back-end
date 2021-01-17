from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = NewsArticle
        fields = ['id','title','category','paragraph',"images",'timestamp']
        lookup_field = 'title'

class VideoLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ['title','youtube_link']
        lookup_field = 'title'
