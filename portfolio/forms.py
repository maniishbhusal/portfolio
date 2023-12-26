from django import forms
from .models import Blog

class UpdateBlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ("title", "image", "description")
