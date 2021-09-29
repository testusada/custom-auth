from django import forms
from .models import Category

class PostForm(forms.Form):
    category_data = Category.objects.all()
    category_choice = {}
    for category in category_data:
        category_choice[category] = category
    title = forms.CharField(max_length=30, label='title')
    category = forms.ChoiceField(choices=list(category_choice.items()),label='カテゴリ',widget=forms.Select)
    content = forms.CharField(label='content', widget=forms.Textarea())
    image = forms.ImageField(label='イメージ画像',required = False )
