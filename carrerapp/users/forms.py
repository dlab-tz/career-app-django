from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'name', 'dob', 'region', 'district', 'phone_no', 'email',
            'oversea', 'country', 'education_level', 'career_field',
            'position', 'work_done', 'organization'
        ]
