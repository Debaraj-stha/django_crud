from django import forms
from my_app.models import myUser,Post,multipleImage


class uploadPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'email', 'password', 'image']
class multipleImageForm(forms.ModelForm):
    class Meta:
        model = multipleImage
        fields = ['images']
        widgets = {
            'images': forms.ClearableFileInput(attrs={'multiple': True}),
        }
        
