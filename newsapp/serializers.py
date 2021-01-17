from .models import *
from rest_framework import serializers
import datetime

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'title'

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    timestamp = serializers.DateTimeField(format="%H")
 
    class Meta:
        model = NewsArticle
        fields = ['id','title','category','paragraph',"images",'timestamp']
        lookup_field = 'title'

class VideoLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ['id','title','youtube_link']
        lookup_field = 'title'
