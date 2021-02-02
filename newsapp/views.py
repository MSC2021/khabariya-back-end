from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from .models import *
from .serializers import *
from urllib.parse import unquote
# Create your views here.

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'title'

class MarqueViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Marque.objects.all()
    serializer_class = MarqueSerializer
    
class NewsAppViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = NewsArticle.objects.all()
    serializer_class = NewsSerializer
    
    def get_queryset(self):
        queryset = NewsArticle.objects.filter(publish=True).order_by('-timestamp')
        category = self.request.query_params.get('category', None)
        search_value = unquote(self.request.query_params.get('search', ''))[:-1]
        if category is not None:
            queryset = queryset.filter(category__title=category).order_by('-timestamp')
        if search_value!='':
            queryset = queryset.filter(title__icontains=search_value).order_by('-timestamp')
        return queryset

class VideoLinkView(generics.ListCreateAPIView):
    queryset = NewsArticle.objects.all().exclude(youtube_link=[])
    serializer_class = VideoLinkSerializer

def PreviewView(request,id):
    try:
        news = NewsArticle.objects.get(id=id)
        category = news.category.all()
        image = ImagesModel.objects.filter(newsArticle=id)
    except:
        return render(request,'preview.html',{'error':'No Object Found'})
    return render(request,'preview.html',{'news':news,'category':category,'image':image})