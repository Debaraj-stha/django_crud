from django import forms
from my_app.models import myUser,Post


class uploadPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'email', 'password', 'image']
        