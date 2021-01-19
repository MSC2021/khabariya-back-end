from .models import *
from rest_framework import serializers
import datetime

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'title'

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesModel
        fields = ['image']
    
class NewsSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    timestamp = serializers.DateTimeField(format="%H")
    images = serializers.SerializerMethodField('get_images')

    def get_images(self, news):
        qs = ImagesModel.objects.filter(newsArticle=news)
        serializer = ImagesSerializer(instance=qs, many=True)
        return serializer.data
    class Meta:
        model = NewsArticle
        fields = ['id','title','category','paragraph','timestamp','youtube_link','images']
        lookup_field = 'title'

class VideoLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ['id','title','youtube_link']
        lookup_field = 'title'


