from django import forms
from  .models import UserProfile
from django_countries.widgets import CountrySelectWidget
from django_countries import countries


class UserProfileForm (forms.ModelForm):
    country = forms.ChoiceField(
        choices=[("", "Select country")] + list(countries),
        required=False,
        widget=CountrySelectWidget(attrs={"id": "country-select"})
    )

    class Meta:
        model = UserProfile
        fields = ['name', 'dob', 'region', 'district','phone_no', 'email',
            'oversea', 'country', 'education_level',
            'career_field', 'position', 'work_done', 'organization', 'upload_cv_file']
        
        widgets = {
             "name":  forms.TextInput(attrs={"class": "form-control"}),
            "dob":   forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),

            "region":   forms.Select(attrs={"id": "region-select", "class": "form-select"}),
            "district": forms.Select(attrs={"id": "district-select", "class": "form-select"}),

            "oversea":  forms.CheckboxInput(attrs={"id": "oversea-check", "class": "form-check-input"}),
            "country":  CountrySelectWidget(attrs={"id": "country-select", "class": "form-select"}),

            "education_level": forms.Select(attrs={"class": "form-select"}),
            "career_field":    forms.Select(attrs={"class": "form-select"}),
            "position":        forms.TextInput(attrs={"class": "form-control"}),
            "work_done":       forms.Textarea(attrs={"class": "form-control", "rows": 3, "id": "work-done"}),
            "organization":    forms.TextInput(attrs={"class": "form-control"}),
            "upload_cv_file":  forms.ClearableFileInput(attrs={'accept': '.pdf,.doc,.docx'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Default country = Tanzania
        self.fields["region"].choices = [("", "Select region")]
        self.fields["district"].choices = [("", "Select district")]