from django import forms
from ckeditor.widgets import CKEditorWidget

from post.models import Post

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=100)
    image = forms.ImageField()
    description = forms.CharField(widget=CKEditorWidget())
    category = forms.IntegerField()

class UpdatePostForm(forms.Form):
    title = forms.CharField(max_length=100)
    image = forms.ImageField(required=False)
    description = forms.CharField(widget=CKEditorWidget())
    category = forms.IntegerField()
