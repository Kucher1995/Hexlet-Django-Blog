from django import forms
from hexlet_django_blog.article.models import Article


class ArticleForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    body = forms.CharField(max_length=200, required=True)
    
    class Meta:
        model = Article
        fields = ['name', 'body']