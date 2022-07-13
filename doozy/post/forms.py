from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','select','video', 'link', 'content']

        widgets = {
            'content': forms.Textarea(attrs={'cols': 20, 'rows': 3})
        }
