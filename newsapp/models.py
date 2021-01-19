from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30)
    visible = models.BooleanField(default = True)
    important = models.BooleanField(default = False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ("वर्ग")
        verbose_name_plural = ("वर्ग")

class NewsArticle(models.Model):
    """
    docstring
    """
    title = models.CharField(max_length=200,verbose_name='शीर्षक')
    paragraph = models.TextField(verbose_name ='विवरण')
    category = models.ManyToManyField(Category,verbose_name='वर्ग')
    youtube_link = ArrayField(models.URLField(blank=True))
    publish = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ("समाचार")
        verbose_name_plural = ("समाचार")

class ImagesModel(models.Model):
    newsArticle = models.ForeignKey(NewsArticle,on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images', blank=True,null=True)
    def __str__(self):
        return self.newsArticle.title
    class Meta:
        verbose_name = ("समाचार तस्वीर")
        verbose_name_plural = ("समाचार तस्वीर")