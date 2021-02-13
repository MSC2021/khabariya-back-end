from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_better_admin_arrayfield.forms.widgets import DynamicArrayTextareaWidget
from django.forms import TextInput, Textarea
from .forms import *
from django.utils.safestring import mark_safe
# Register your models here.
class MyNewsAdmin(admin.ModelAdmin, DynamicArrayMixin):
    form = NewsForm
    search_fields = ('title',)
    list_filter = ('publish','category',)
    filter_horizontal =('category',)
    readonly_fields = ('timestamp',)
    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size':'40'})},
        models.TextField: {'widget': Textarea(attrs={'rows':20, 'cols':150})},
    }
    def get_absolute_url(self):
        return "/preview/%i/" % 1

    def preview_template(self,obj):
        return mark_safe("<a href='/preview/%d/' target='_blank'>View</a>" % obj.id)
    preview_template.short_description = 'Preview'
    list_display = ('title','preview_template','timestamp')
   
    def get_fields(self,request,obj=None):
        if request.user.is_superuser or request.user.groups.filter(name='Senior Reporter').exists():
            fields = ['title','paragraph','category','youtube_link','images','key_words','publish',]
        else:
            fields = ['title','paragraph','category','youtube_link','images','key_words',]
        return fields

class AdvertisementAdmin(admin.ModelAdmin,DynamicArrayMixin):
    search_fields = ('title',)
    readonly_fields = ('timestamp',)
    list_display = ('title','timestamp',)
    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size':'40'})},
        models.TextField: {'widget': Textarea(attrs={'rows':20, 'cols':150})},
    }
class CategryAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    readonly_fields = ('timestamp',)
    list_display = ('title','timestamp',)
    list_filter = ('visible','important',)
    
admin.site.register(NewsArticle,MyNewsAdmin)
admin.site.register(ImagesModel)
admin.site.register(Category,CategryAdmin)
admin.site.register(Marque)
admin.site.register(VideoNews)
admin.site.register(Advertisment,AdvertisementAdmin)
admin.site.register(keyWord)
admin.site.site_header = "Khabariya Panel"
admin.site.site_title = "Khabariya "