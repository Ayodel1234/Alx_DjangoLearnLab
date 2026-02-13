from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from .models import Comment
from .models import Post, Tag




class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Comma-separated tags")

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

            tags_data = self.cleaned_data['tags']
            tag_list = [tag.strip() for tag in tags_data.split(',') if tag.strip()]

            instance.tags.clear()

            for tag_name in tag_list:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                instance.tags.add(tag)

        return instance



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
