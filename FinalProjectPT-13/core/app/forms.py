from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('user', 'title', 'category', 'image', 'description', 'price', 'phone_number', 'condition')


class PostUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'category', 'image', 'description', 'price', 'phone_number', 'condition')


