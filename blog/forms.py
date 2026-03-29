
from blog.models import Post, Blog_Comment
from django import forms


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tegs','image']

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Blog_Comment
        fields = ['text']