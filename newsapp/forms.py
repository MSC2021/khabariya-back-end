from django import forms
from django.core.exceptions import ValidationError
from .models import *

class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsArticle
        fields = '__all__'
    def clean(self):
        """
        Checks that all the words belong to the sentence's language.
        """
        categories = self.cleaned_data.get('category')
        flag= True
        for category in categories:
            if category.title!='home' and category.title!='slider':
                flag = False
        if flag:
            raise ValidationError("Home or Slider category cannot be used alone please another category as well")
        return self.cleaned_data