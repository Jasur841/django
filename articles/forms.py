from django import forms

from . import models


class ArticleCreateForm(forms.ModelForm):
    author = forms.HiddenInput()

    class Meta:
        model = models.Article
        fields = [
            'title',
            'body',
            'author',
        ]
