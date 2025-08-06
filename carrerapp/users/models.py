from django.db import models

class UserProfile(models.Model):
    CAREER_CHOICES = [
        ('software_engineer', 'Software Engineer'),
        ('data_scientist', 'Data Scientist'),
        ('web_developer', 'Web Developer'),
        ('network_admin', 'Network Administrator'),
        ('teacher', 'Teacher'),
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('accountant', 'Accountant'),
        ('lawyer', 'Lawyer'),
        ('engineer', 'Engineer'),
        ('mechanic', 'Mechanic'),
        ('chef', 'Chef'),
        ('pilot', 'Pilot'),
        ('artist', 'Artist'),
        ('musician', 'Musician'),
        ('entrepreneur', 'Entrepreneur'),
        ('architect', 'Architect'),
        ('pharmacist', 'Pharmacist'),
        ('civil_servant', 'Civil Servant'),
        ('journalist', 'Journalist'),
        ('other', 'Other')
    ]

    EDUCATION_LEVEL_CHOICES = [
        ('none', 'None'),
        ('olevel', 'O Level'),
        ('alevel', 'A Level'),
        ('diploma', 'Diploma'),
        ('bachelors', 'Bachelors Degree'),
        ('masters', 'Masters Degree'),
        ('phd', 'PhD')
    ]

    name = models.CharField(max_length=100)
    education_level = models.CharField(max_length=20, choices=EDUCATION_LEVEL_CHOICES)
    career_field = models.CharField(max_length=50, choices=CAREER_CHOICES)

    
    works_locally = models.BooleanField(default=True)
    works_overseas = models.BooleanField(default=False)
    region = models.CharField(max_length=100, blank=True, null=True)  # For local workers
    country = models.CharField(max_length=100, blank=True, null=True)  # For overseas workers

def __str__(self):
        return self.name