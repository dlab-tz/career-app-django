from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'dob', 'region', 'district', 'email', 'career_field',
        'education_level', 'organization', 
    )
    search_fields = ('name', 'email', 'career_field')
    list_filter = ('education_level', 'career_field')
