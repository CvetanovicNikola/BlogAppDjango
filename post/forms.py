from django import forms
from .model import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",  "email", "image", "text", "image2", "text2", "image3", "text3"
        ]
        #"address", "price",