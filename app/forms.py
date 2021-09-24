from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='title')
    content = forms.CharField(label='content', widget=forms.Textarea())
