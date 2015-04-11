from django import forms
from django.contrib.auth.models import User
from blog.models import Post, Comment


class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput())

  class Meta:
    model = User
    fields = ('username', 'email', 'password')

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ( 'content',)

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('content',)

