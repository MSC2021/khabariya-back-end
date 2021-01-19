from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django_better_admin_arrayfield.forms.widgets import DynamicArrayTextareaWidget
from django.forms import TextInput, Textarea
# Register your models here.
class MyNewsAdmin(admin.ModelAdmin, DynamicArrayMixin):
    filter_horizontal =('category',)
    readonly_fields = ('timestamp',)
    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size':'40'})},
        models.TextField: {'widget': Textarea(attrs={'rows':20, 'cols':150})},
    }
    def get_fields(self,request,obj=None):
        if request.user.is_superuser:
            fields = ['title','paragraph','category','youtube_link','publish']
        else:
            fields = ['title','paragraph','category','youtube_link',]
        return fields

admin.site.register(NewsArticle,MyNewsAdmin)
admin.site.register(ImagesModel)
admin.site.register(Category)