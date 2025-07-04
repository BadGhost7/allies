from django import forms
from .models import Profile
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from .models import UserProfile
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'discord', 'steam_profile']
        widgets = {
            'discord': forms.TextInput(attrs={'placeholder': 'Username#0000'}),
            'steam_profile': forms.URLInput(attrs={'placeholder': 'https://steamcommunity.com/id/username'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'game_preferences', 'skill_level', 'is_public']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }