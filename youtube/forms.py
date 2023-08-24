from django.forms import ModelForm
from django import forms
from .models import Video, Comment


class VideoForm(ModelForm):
    class Meta:
        model = Video
        fields = ["author", "title", "thumbnail", "icon", "content"]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "content"]
