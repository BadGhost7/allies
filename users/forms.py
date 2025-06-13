from django import forms
from .models import Profile

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'discord', 'steam_profile']
        widgets = {
            'discord': forms.TextInput(attrs={'placeholder': 'Username#0000'}),
            'steam_profile': forms.URLInput(attrs={'placeholder': 'https://steamcommunity.com/id/username'}),
        }
