from django import forms
from .models import Profile
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'discord', 'steam_profile']
        widgets = {
            'discord': forms.TextInput(attrs={'placeholder': 'Username#0000'}),
            'steam_profile': forms.URLInput(attrs={'placeholder': 'https://steamcommunity.com/id/username'}),
        }

class ProfileForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']