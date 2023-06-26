from django import forms

from .models import Item

inputCSS = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={'class': inputCSS}),
            'name': forms.TextInput(attrs={'class': inputCSS}),
            'description': forms.Textarea(attrs={'class': inputCSS}),
            'price': forms.TextInput(attrs={'class': inputCSS}),
            'image': forms.FileInput(attrs={'class': inputCSS}),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'isSold')

        widgets = {
            'category': forms.Select(attrs={'class': inputCSS}),
            'name': forms.TextInput(attrs={'class': inputCSS}),
            'description': forms.Textarea(attrs={'class': inputCSS}),
            'price': forms.TextInput(attrs={'class': inputCSS}),
            'image': forms.FileInput(attrs={'class': inputCSS}),
        }

