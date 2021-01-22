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
        if request.user.is_superuser:
            fields = ['title','paragraph','category','youtube_link','publish',]
        else:
            fields = ['title','paragraph','category','youtube_link',]
        return fields

admin.site.register(NewsArticle,MyNewsAdmin)
admin.site.register(ImagesModel)
admin.site.register(Category)
admin.site.register(Marque)
admin.site.site_header = "Khabariya Panel"
admin.site.site_title = "Khabariya "