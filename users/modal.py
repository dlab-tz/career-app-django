from django.db import models

class UserProfile(models.Model):
    EDUCATION_LEVEL_CHOICES = [
        ('primary', 'Primary'),
        ('secondary', 'Secondary'),
        ('diploma', 'Diploma'),
        ('bachelor', 'Bachelor’s Degree'),
        ('masters', 'Master’s Degree'),
        ('phd', 'PhD'),
    ]

    username = models.CharField(max_length=150, unique=True)
    education_level = models.CharField(max_length=20, choices=EDUCATION_LEVEL_CHOICES)
    career_field = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username} - {self.career_field}"

