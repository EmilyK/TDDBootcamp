from django import forms

class CreatePostForm(forms.Form):
   title = forms.CharField(max_length=40, required=True)
   body = forms.CharField()