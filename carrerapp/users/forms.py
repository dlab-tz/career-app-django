from django import forms
from  .models import UserProfile

class UserProfileForm (forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'works_overseas', 'region', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'region': forms.TextInput(attrs={'placeholder': 'Enter your region'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter your country'}),
        }