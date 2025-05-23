from django import forms
from .models import Blog, Author

class BlogForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Select the author")

    class Meta:
        model = Blog
        fields = ['title', 'content', 'author', 'image']


