from django.db import models
from django_better_admin_arrayfield.models.fields import ArrayField
# Create your models here.

from django.core.mail import send_mail


class Category(models.Model):
    title = models.CharField(max_length=30)
    visible = models.BooleanField(default = True)
    important = models.BooleanField(default = False)
    timestamp = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ("वर्ग")
        verbose_name_plural = ("वर्ग")

class ImagesModel(models.Model):
    # newsArticle = models.ForeignKey(NewsArticle,on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images',default='image.jpg')
    def __str__(self):
        return str(self.image)
    class Meta:
        verbose_name = ("समाचार तस्वीर")
        verbose_name_plural = ("समाचार तस्वीर")

class keyWord(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
        
class NewsArticle(models.Model):
    title = models.CharField(max_length=200,verbose_name='शीर्षक')
    paragraph = models.TextField(verbose_name ='विवरण')
    category = models.ManyToManyField(Category,verbose_name='वर्ग')
    youtube_link = ArrayField(models.URLField(blank=True),blank=True,null=True)
    publish = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)
    images = models.ManyToManyField(ImagesModel)
    key_words = models.ManyToManyField(keyWord,blank=True)

    def save(self, *args, **kwargs):
        created = self.pk is None
        super().save(*args, **kwargs)
        if created:
            send_mail('New news added',self.title+' -'+self.paragraph,'chinmay123456789@gmail.com',['chinmay123456789@gmail.com',])
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ("समाचार")
        verbose_name_plural = ("समाचार")

class Marque(models.Model):
    title = models.CharField(max_length =100)
    timestamp = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ("Ticker")
        verbose_name_plural = ("Tickers")

class VideoNews(models.Model):
    title = models.CharField(max_length=200,verbose_name='शीर्षक')
    youtube_link = models.URLField()
    timestamp = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = ("वीडियो समाचार")
        verbose_name_plural = ("वीडियो समाचार")

class Advertisment(models.Model):
    title = models.CharField(max_length=200,verbose_name='शीर्षक')
    paragraph = models.TextField(verbose_name ='विवरण')
    youtube_link = ArrayField(models.URLField(),blank=True,null=True)
    image = models.ImageField(upload_to='images', blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ("विज्ञापन")
        verbose_name_plural = ("विज्ञापन")

class Career(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True,blank=True)
    mobile_no = models.CharField(max_length=13)
    location = models.CharField(max_length = 200)
    resume = models.FileField(blank=True,null=True)

    def __str__(self):
        return self.name
    