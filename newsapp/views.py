from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework.response import Response
from .models import *
from .serializers import *
from urllib.parse import unquote
# Create your views here.

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('-timestamp')
    serializer_class = CategorySerializer
    lookup_field = 'title'

class MarqueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Marque.objects.all().order_by('-timestamp')
    serializer_class = MarqueSerializer
    
class NewsAppViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsSerializer
    
    def get_queryset(self):
        queryset = NewsArticle.objects.filter(publish=True).order_by('-timestamp')
        category = self.request.query_params.get('category', None)
        search_value = unquote(self.request.query_params.get('search', ''))[:]
        if category is not None:
            queryset = queryset.filter(category__title=category).order_by('-timestamp')
        if search_value!='':
            queryset = queryset.filter(title__icontains=search_value) | queryset.filter(key_words__title__icontains=search_value) | queryset.filter(category__title=search_value)
            queryset = queryset.distinct().order_by('-timestamp')
        return queryset

class VideoLinkView(generics.ListCreateAPIView):
    queryset = NewsArticle.objects.all().exclude(youtube_link=[]).order_by('-timestamp')
    serializer_class = VideoLinkSerializer

    def list(self, request, *args, **kwargs):
        result1 = self.serializer_class(self.get_queryset(),many=True)
        result2 = VideoNewsSerializer(VideoNews.objects.all().order_by('-timestamp'),many=True)
        return Response(result2.data+result1.data)
        
# class VideoNewsView(generics.ListCreateAPIView):
#     queryset = VideoNews.objects.all()
#     serializer_class = VideoNewsSerializer
#     def list(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)

class AdvertismentView(generics.ListCreateAPIView):
    queryset = Advertisment.objects.all().order_by('-timestamp')
    serializer_class = AdvertismentSerializer

def PreviewView(request,id):
    try:
        news = NewsArticle.objects.get(id=id)
        category = news.category.all()
        image = ImagesModel.objects.filter(newsArticle=id)
    except:
        return render(request,'preview.html',{'error':'No Object Found'})
    return render(request,'preview.html',{'news':news,'category':category,'image':image})