from django import forms
from  .models import UserProfile

class UserProfileForm (forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'dob', 'region', 'district','phone_no', 'email',
            'oversea', 'country', 'education_level',
            'career_field', 'position', 'work_done', 'organization']
        
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'region': forms.TextInput(attrs={'placeholder': 'Enter your region'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter your country'}),
        }