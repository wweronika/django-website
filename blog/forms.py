from django import forms

from .models import Post, Project

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text','image',)

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title', 'technology', 'description', 'image',)