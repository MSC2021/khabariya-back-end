from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30)

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
    paragraph = ArrayField(models.CharField(max_length=400),verbose_name ='विवरण')
    category = models.ManyToManyField(Category,verbose_name='वर्ग')
    images = models.ImageField(upload_to='images', blank=True,null=True)
    youtube_link = models.URLField(blank=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ("समाचार")
        verbose_name_plural = ("समाचार")