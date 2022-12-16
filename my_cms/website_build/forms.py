from django import forms
from .models import Website

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = [
        # "user",
        "title",
        "occupation",
        "about_me",
        "skill1",
        "skill2",
        "skill3",
        "skill4",
        "fb",
        "twitter",
        ]

        widgets = {
            # 'user': forms.TextInput(attrs={'class': 'form-control',}),
            'title': forms.TextInput(attrs={'class': 'form-control',  'placeholder': "Title here", 'required': True}),
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "e.g Web Developer", 'required': True}),
            'about_me': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 100px', 'placeholder': "I'm a web developer .....", 'required': True}),
            'skill1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "e.g Python"}),
            'skill2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "e.g HTML"}),
            'skill3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "e.g CSS"}),
            'skill4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "e.g JavaScript"}),
            'fb': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "facebook.com/abdul"}),
            'twitter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "twitter.com/abdul"}),
        }
